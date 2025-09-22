from setuptools import find_packages, setup

package_name = 'robot_controller_sept_03'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ws',
    maintainer_email='yg4776@srmist.edu.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_node = robot_controller_sept_03.my_first_node:main',
            'draw_circle = robot_controller_sept_03.draw_circle:main'
        ],
    },
)
