from setuptools import setup, find_packages

setup(
    name="main",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Click",
    ],
    entry_points={
        'console_scripts': [
            'bruno=bruno.main:cli',
        ],
    },
)
# remove this hehe