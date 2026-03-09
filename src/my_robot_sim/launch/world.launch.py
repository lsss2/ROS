import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 1. Get the absolute path to your world file
    my_world_path = os.path.join(
        get_package_share_directory('my_robot_sim'),
        'worlds',
        'car.world'
    )

    # 2. Path to the PAL TIAGo launch file
    tiago_gazebo_dir = get_package_share_directory('tiago_gazebo')

    # 3. FORCE Gazebo to see your package's worlds folder
    # This is the "Nuclear Option" that fixes the 'World not found' error
    gazebo_path_env = SetEnvironmentVariable(
        'GAZEBO_RESOURCE_PATH', 
        os.path.join(get_package_share_directory('my_robot_sim'), 'worlds') + ':' + os.environ.get('GAZEBO_RESOURCE_PATH', '')
    )
    
    tiago_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tiago_gazebo_dir, 'launch', 'tiago_gazebo.launch.py')
        ),
        launch_arguments={
            'is_public_sim': 'True',
            'world_name': my_world_path, # Pass the full absolute path
            'gzx': '2.0',
            'gzy': '2.0'
        }.items()
    )

    return LaunchDescription([
        gazebo_path_env,
        tiago_sim
    ])
