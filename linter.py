#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by admin
# Copyright (c) 2016 admin
#
# License: MIT
#

"""This module exports the Ycmd plugin class."""
import os
import sublime
from SublimeLinter.lint import PythonLinter, util
from .lib.ycmd_handler import server

class Ycmd(PythonLinter):
    """Provides an interface to ycmd."""

    syntax = 'python'
    cmd = None
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
    module = 'ycmd'
    check_version = False
    def check(self, code, filename):
        print(filename)

