#!/usr/bin/env python
from distutils.core import setup

DATAFILES = [('/usr/share/man/man1', ['namcapp.1'])]

setup(name="namcap",
	version="2.0",
	description="Pacman package analyzer",
	author="Jason Chu",
	author_email="jason@archlinux.org",
	py_modules=["pacmanp"], packages=["Namcapp"], scripts=["namcapp.py", 'parsepkgbuildp'],data_files =DATAFILES)

# vim: set ts=4 sw=4 noet:
