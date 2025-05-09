from setuptools import setup, find_packages

setup(
    name="bruno",  
    version="0.1.0",
    author="Dawson Hassell",
    description="A handy and lightweight CLI tool for logging and exporting your personal experiences like restaurants, parks, coffee shops, and more.",
    packages=find_packages(),
    install_requires=[
        "Click",
    ],
    entry_points={
        'console_scripts': [
            'bruno=bruno.main:cli', 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)