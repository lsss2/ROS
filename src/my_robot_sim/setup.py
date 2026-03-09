from setuptools import setup
import os           # <--- IMPORTANTE
from glob import glob # <--- IMPORTANTE

package_name = 'my_robot_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    # This line handles the launch files
    (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    # This line handles the world files
    (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
    (os.path.join('share', package_name, 'navigation'), glob('navigation/*.yaml')),
    (os.path.join('share', package_name, 'navigation'), glob('navigation/*.rviz')),
    (os.path.join('share', package_name, 'navigation'), glob('navigation/*.py')), # for SLAM_launch.py
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tu_nombre',
    maintainer_email='tu@email.com',
    description='Simulacion del robot en mundo XML',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Aquí irán tus scripts de control más adelante
        ],
    },
)
