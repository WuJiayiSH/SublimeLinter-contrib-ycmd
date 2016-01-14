import os
import sublime
from .lib.ycmd_handler import server
from .lib.utils import *

exists = check_ycmd_server()
if exists:
	print("ok")

server(view.file_name())