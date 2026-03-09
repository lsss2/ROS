import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'my_robot_sim'
    pkg_share = get_package_share_directory(package_name)
    
    # Ruta al URDF (Asegúrate de que este archivo existe en la carpeta install)
    urdf_path = os.path.join(pkg_share, 'urdf', 'tiago_ligero.urdf')

    # 1. Robot State Publisher (Sigue siendo necesario para que RViz vea al robot)
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 2. Spawn Entity (Ahora leyendo directamente desde el archivo .urdf)
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-file', urdf_path,    # <--- Cambio clave: leemos el archivo directamente
            '-entity', 'tiago', 
            '-x', '2.0', '-y', '2.0', '-z', '0.2'
        ],
        output='screen'
    )

    return LaunchDescription([rsp, spawn_entity])
