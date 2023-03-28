from setuptools import setup, find_packages

setup(
    name='cokilogin',
    version='0.1.0',
    description='A Python script for logging into websites using HTTP Cookies and Requests',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'cokilogin = cokilogin.__main__:main'
        ]
    }
)
