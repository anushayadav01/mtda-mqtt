#!/usr/bin/python3
#-------------------------------------------------------------
#Setup script for MTDA-MQTT
#-------------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name='mtda_mqtt',
    packages=find_packages(),
    version='1.0.0',
    scripts=['mtda-mqtt-cli'],
    description='Multi-Tenant Devices Access-MQTT',
    url='https://github.com/anushayadav01/mtda-mqtt',
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Embedded Systems",
    ],

    install_requires=[
        "python-daemon>=2.0",
        "paho-mqtt",
        "socket",
        "zerorpc>=0.6.0"
    ],
)
