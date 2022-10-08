from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Encrypt strings to the Bee Movie script and back'

# Setting up
setup(
    name="beencrypted",
    version=VERSION,
    author="Agent-Kwabbel (Fabe Stuffken)",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'bee', 'movie', 'bee movie', 'encryption', 'decryption', 'meme'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)