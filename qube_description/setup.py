from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'qube_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oyste',
    maintainer_email='oysteindale@live.com',
    description='URDF/Xacro description of the Quanser Qube.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={},
)