
from setuptools import setup

setup(name="light_tester",
    version="0.1",
    description="Light board tester",
    url="",
    author="Elena Lanigan",
    author_email="elenalanigan93@gmail.com",
    license="GPL3",
    packages=['light_tester'],
    entry_points={
        'console_scripts':['countLights=light_tester.light_tester:main']
        }   
    
)