import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 1. Definir rutas
    pkg_my_sim = get_package_share_directory('my_robot_sim')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    
    world_path = os.path.join(pkg_my_sim, 'worlds', 'car.world')
    urdf_path = os.path.join(pkg_my_sim, 'urdf', 'robot.urdf')

    # 2. Configurar variables de entorno (CRITICO para evitar el cierre de Gazebo)
    # Gazebo necesita saber dónde están tus modelos y tus mundos
    set_resource_path = SetEnvironmentVariable(
        'GAZEBO_RESOURCE_PATH', 
        os.path.join(pkg_my_sim, 'worlds') + ':' + os.environ.get('GAZEBO_RESOURCE_PATH', '')
    )
    
    set_model_path = SetEnvironmentVariable(
        'GAZEBO_MODEL_PATH',
        os.path.join(pkg_my_sim, 'urdf') + ':' + os.environ.get('GAZEBO_MODEL_PATH', '')
    )

    # 3. Lanzar Gazebo (Servidor y Cliente juntos)
    # Usar el launch oficial de gazebo_ros es más estable
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_path}.items()
    )

    # 4. Robot State Publisher
    # Esto lee el URDF y lo publica en el tópico /robot_description
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 5. Spawn Entity (El que mete el robot en Gazebo)
    # Lo tomamos del tópico para evitar problemas de rutas de archivo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'mi_robot', '-topic', 'robot_description', '-z', '0.2'],
        output='screen'
    )

    return LaunchDescription([
        set_resource_path,
        set_model_path,
        gazebo,
        rsp,
        spawn_entity
    ])
