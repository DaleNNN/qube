import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, Float64MultiArray
from sensor_msgs.msg import JointState


class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')

        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

        self.target_subscription = self.create_subscription(
            Float64,
            '/target_position',
            self.target_callback,
            10
        )

        self.publisher = self.create_publisher(
            Float64MultiArray,
            '/velocity_controller/commands',
            10
        )

        self.timer = self.create_timer(0.02, self.control_loop)

        self.kp = 2.0
        self.ki = 0.0
        self.kd = 0.2

        self.target_position = 0.0
        self.position = 0.0
        self.velocity = 0.0
        self.have_state = False

        self.integral = 0.0
        self.prev_error = 0.0
        self.last_time = self.get_clock().now()

        self.max_command = 3.0

    def target_callback(self, msg: Float64):
        self.target_position = msg.data
        self.get_logger().info(f'Ny referanse: {self.target_position:.3f} rad')

    def joint_state_callback(self, msg: JointState):
        if 'motor_joint' not in msg.name:
            return

        i = msg.name.index('motor_joint')
        self.position = msg.position[i]

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

        error = self.target_position - self.position
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt

        u = self.kp * error + self.ki * self.integral + self.kd * derivative
        u = max(min(u, self.max_command), -self.max_command)

        msg = Float64MultiArray()
        msg.data = [u]
        self.publisher.publish(msg)

        self.prev_error = error
        self.last_time = now


def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()