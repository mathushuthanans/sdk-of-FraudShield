from setuptools import setup, find_packages

setup(
    name='adci-botdetector',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
    ],
    author='Mathu',
    description='SDK for detecting bot behavior using keystroke and mouse metrics.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
