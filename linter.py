#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Administrator
# Copyright (c) 2016 Administrator
#
# License: MIT
#

"""This module exports the Ycmd plugin class."""

import os
import re
import json
from SublimeLinter.lint import highlight, Linter, persist
from .lib.ycmd_handler import server
from .lib.utils import *
from .lib.ycmd_events import Event
from .lib.msgs import MsgTemplates
from .listeners import *
class Ycmd(Linter):
    """Provides an interface to ycmd."""
    syntax = ('c++', 'c', 'c improved')  # Able to handle C and C++ syntax
    cmd = None
    regex = '.*'  # Placeholder so that linter will activate

    selectors = {
        
    }

    defaults = {
        '-errors:,': [],
        '-warnings:,': []
    }


    # regex = r''
    # defaults = {}
    def run(self, cmd, code):
        

        view = active_view()
        filepath = get_file_path(view.file_name())
        contents = view.substr(sublime.Region(0, view.size()))

        ycmd_server = server(self.filename)
        # conf_path = find_recursive(filepath)
        # if not conf_path:
        #     sublime.status_message(
        #         '[SublimeLinter-contrib-ycmd] .ycm_extra_conf.py not found. All SublimeLinter-contrib-ycmd function not avaliable.')
        #     print('[SublimeLinter-contrib-ycmd] .ycm_extra_conf.py not found.')
        #     return
            
        # ycmd_server.LoadExtraConfFile(conf_path)

        data = ycmd_server.SendEventNotification(Event.FileReadyToParse,
                                        filepath=filepath,
                                        contents=contents,
                                        filetype='cpp')
        print(data)

        options = {}

        type_map = {
            'errors': [],
            'warnings': []
        }

        self.build_options(options, type_map)

        problems = json.loads(data)
        
        for problem in problems:
            if get_file_path(problem['location']['filepath']) == filepath:
                lineno = problem['location']['line_num'] - 1
                colno = problem['location']['column_num'] - 1
                message = problem['text']

                error_type = highlight.WARNING
                if problem['kind'] == 'ERROR':
                    error_type = highlight.ERROR
                
                
                self.highlight.range(lineno, colno, error_type=error_type)
                self.error(lineno, colno, message, error_type)

