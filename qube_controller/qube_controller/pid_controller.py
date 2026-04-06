import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, Float64MultiArray
from sensor_msgs.msg import JointState


class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')

        # Leser tilstand fra Quben
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

        # Leser ønsket vinkel
        self.target_subscription = self.create_subscription(
            Float64,
            '/target_position',
            self.target_callback,
            10
        )

        # Sender hastighetskommando til kontroller
        self.publisher = self.create_publisher(
            Float64MultiArray,
            '/velocity_controller/commands',
            10
        )

        # Kontroll-loop (50 Hz)
        self.timer = self.create_timer(0.02, self.control_loop)

        # PID gains
        self.kp = 2.0
        self.ki = 0.0
        self.kd = 0.1

        # Tilstand
        self.target_position = 0.0
        self.position = 0.0
        self.velocity = 0.0
        self.have_state = False

        # PID intern tilstand
        self.integral = 0.0
        self.last_time = self.get_clock().now()

        # Begrensninger
        self.max_command = 100.0
        self.max_integral = 2.0
        self.output_scale = 10.0

        # Reduser logging
        self.debug_counter = 0

    @staticmethod
    def wrap_to_pi(angle: float) -> float:
        # Sikrer korteste vei rundt sirkelen
        return (angle + math.pi) % (2 * math.pi) - math.pi

    def target_callback(self, msg: Float64):
        self.target_position = msg.data

        # Reset integrator ved ny referanse
        self.integral = 0.0

        self.get_logger().info(f'Ny referanse: {self.target_position:.3f} rad')

    def joint_state_callback(self, msg: JointState):
        # Henter tilstand for motor_joint
        if 'motor_joint' not in msg.name:
            return

        i = msg.name.index('motor_joint')
        self.position = msg.position[i]

        # Håndterer tilfelle uten velocity
        if len(msg.velocity) > i:
            self.velocity = msg.velocity[i]
        else:
            self.velocity = 0.0

        self.have_state = True

    def control_loop(self):
        if not self.have_state:
            return

        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds / 1e9

        if dt <= 0.0:
            return

        # Feil (korteste vei)
        error = self.wrap_to_pi(self.target_position - self.position)

        # Integrator (med begrensning)
        self.integral += error * dt
        self.integral = max(min(self.integral, self.max_integral), -self.max_integral)

        # PID (D basert på målt hastighet)
        u_unsat = self.kp * error + self.ki * self.integral - self.kd * self.velocity

        # Skalering og metning
        u = self.output_scale * u_unsat
        u = max(min(u, self.max_command), -self.max_command)

        # Publiser kommando
        msg = Float64MultiArray()
        msg.data = [u]
        self.publisher.publish(msg)

        self.last_time = now

        # Periodisk logging
        self.debug_counter += 1
        if self.debug_counter >= 10:
            self.get_logger().info(
                f'pos={self.position:.3f} rad, '
                f'vel={self.velocity:.3f} rad/s, '
                f'target={self.target_position:.3f} rad, '
                f'err={error:.3f} rad, '
                f'u={u:.3f}'
            )
            self.debug_counter = 0


def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()