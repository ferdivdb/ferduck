'''
author : ferdivdb
date : 19/12/2021

'''
from setuptools import setup

APP=['app.py']
OPTIONS = {
	'argv_emulation': True,
}

setup(
	app=APP,
	options={'py2app': OPTIONS},
	setup_requires=['py2app']
)

# command in term to convert : sudo python3 setup.py py2app