from setuptools import setup, find_packages
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='askai',  
    version='1.1',
    packages=find_packages(),
    install_requires=[REQUIREMENTS], 
    entry_points={
        'console_scripts': [
            'askai=askai.askai:main', 
        ],
    },
)