from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    baud_rate = LaunchConfiguration("baud_rate")
    device = LaunchConfiguration("device")
    simulation = LaunchConfiguration("simulation")

    robot_description = Command([
        "xacro ",
        PathJoinSubstitution([
            FindPackageShare("qube_bringup"),
            "urdf",
            "controlled_qube.urdf.xacro"
        ]),
        " baud_rate:=", baud_rate,
        " device:=", device,
        " simulation:=", simulation,
    ])

    qube_driver_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("qube_driver"),
                "launch",
                "qube_driver.launch.py"
            ])
        ),
        launch_arguments={
            "baud_rate": baud_rate,
            "device": device,
            "simulation": simulation,
        }.items()
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}],
        output="screen",
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument("baud_rate", default_value="115200"),
        DeclareLaunchArgument("device", default_value="/dev/ttyACM0"),
        DeclareLaunchArgument("simulation", default_value="false"),
        qube_driver_launch,
        robot_state_publisher,
        rviz,
    ])