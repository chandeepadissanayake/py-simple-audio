# Simpleaudio Python Extension
# Copyright (C) 2015, Joe Hamilton 
# MIT License (see LICENSE.txt)

#from distutils.core import setup, Extension
from setuptools import setup, Extension
import sys

platform_sources = []
platform_libs = []
platform_link_args = []

if sys.platform == 'darwin':
    platform_sources = ['simpleaudio_mac.c', 'posix_mutex.c']
    platform_link_args = ['-framework', 'AudioToolbox']
elif sys.platform == 'linux':
    platform_sources = ['simpleaudio_alsa.c', 'posix_mutex.c']
    platform_libs = ['asound']
elif sys.platform == 'win32':
    platform_sources = ['simpleaudio_win.c', 'windows_mutex.c']
    platform_libs = ['Winmm', 'User32']
else:
    pass
    # define a compiler macro for unsupported ?

_simpleaudio_module = Extension(
    '_simpleaudio',
    sources=platform_sources+['simpleaudio.c'],
    libraries=platform_libs,
    extra_link_args=platform_link_args,
    define_macros = [('DEBUG', '1')])

_VERSION = "0.1.0"

setup(
    name = 'simpleaudio',
    packages = ['simpleaudio'],
    version = _VERSION,
    description = """The simpleaudio package contains the simpleaudio module
                     which makes playing wave audio in Python very simple.""",
    author = 'Joe Hamilton',
    author_email = 'jhamilton10@georgefox.edu',
    url = 'https://github.com/hamiltron/simpleaudio', 
    download_url = 'https://github.com/hamiltron/simpleaudio/tarball/'+_VERSION, 
    keywords = ['audio', 'wave', 'media', 'multimedia', 'sound', 'alsa', 'coreaudio', 'winmm', 'music'], 
    classifiers = [],
    test_suite="tests",
    py_modules = ["simpleaudio.shiny"],
    ext_modules = [_simpleaudio_module])
