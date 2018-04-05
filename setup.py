#!/usr/bin/env python

from distutils.core import setup, Extension
import sys

if sys.version_info < (3,5):
    macro_list = [ ( "PYTHON_VERSION_OLDER_THREE_FIVE", "1" ) ]
else:
    macro_list = [ ]

setup(
    name = 'PyQNormaliz',
    version = '0.1',
    description = 'An interface to Normaliz',
    author = 'Sebastian Gutsche, Richard Sieg',
    author_email = 'sebastian.gutsche@gmail.com',
    url = 'https://github.com/Normaliz/PyQNormaliz',
    ext_modules = [ Extension( "PyQNormaliz_cpp",
                              [ "QNormalizModule.cpp" ],
                              extra_compile_args=['-I/home/sebastian/Dokumente/projects/Normaliz/worktree-enfnormaliz/nmz_opt_lib/include', '-L/home/sebastian/Dokumente/projects/Normaliz/worktree-enfnormaliz/nmz_opt_lib/lib'],
                              extra_link_args=['-lQnormaliz', '-lgmp' ],
                              define_macros = macro_list ) ],
    
    package_data = {'': [ "COPYING", "GPLv2", "Readme.md" ] },
)
