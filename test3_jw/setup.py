from setuptools import find_packages, setup

package_name = 'test3_jw'

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
    maintainer='junwoo',
    maintainer_email='dlawnsdn0525@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test3_jw_sub = test3_jw.test3_jw_sub_helloworld:main'
        ],
    },
)
