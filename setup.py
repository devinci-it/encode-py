from setuptools import setup, find_packages

setup(
    name="encoder",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project needs
    ],
    entry_points={
        'console_scripts': [
            'encoder = app.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
