from setuptools import setup, find_packages

setup(
    name="suprascript",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'suprascript=src.interpreter:main',
        ],
    },
)
