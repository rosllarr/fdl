from setuptools import setup

setup(
    name='fdl',
    version='0.1.0',
    packages=['fdl'],
    entry_points={
        'console_scripts': [
            'fdl = fdl.__main__:main'
        ]
    })
