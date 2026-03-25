from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():
    package_share = get_package_share_directory("qube_description")

    xacro_file = os.path.join(
        package_share,
        "urdf",
        "qube.urdf.xacro"
    )

    rviz_config_file = os.path.join(
        package_share,
        "config",
        "qube_config.rviz"
    )

    robot_description_content = xacro.process_file(xacro_file).toxml()

    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content}]
    )

    return LaunchDescription([
        node_rviz,
        node_robot_state_publisher
    ])