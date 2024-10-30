import sys
import os
import cx_Freeze

os.environ["TCL_LIBRARY"] = "C:\\Program Files\\Python310\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Program Files\\Python310\\tcl\\tk8.6"

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("calculator.pyw", base = "Win32GUI")]

cx_Freeze.setup(
    name = "calculator",
    options = {"build.exe":{"packages":["tkinter"], "include_files":["H:\\s3\\computing science\\\python\\4 misc\\icon.ico", "C:\\Program Files\\Python310\\DLLs\\tcl86t.dll", "C:\\Program Files\\Python310\\DLLs\\tk86t.dll"]}},
    version = "0.1",
    executables=executables)
