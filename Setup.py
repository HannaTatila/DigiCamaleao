import os
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
   "packages": ["os","pygame","cx_Freeze", "Pil", "pip"],
   "include_files": ["recursos"]
}

setup(
   name = "Maremoto",
    version = "1.0",
    description = "Maremoto",
    options = {"build_exe": build_exe_options},
    executables = [Executable(os.path.join("principal", "App.py"), targetName="Maremoto.exe", shortcutName="Maremoto", shortcutDir="DesktopFolder", base=base, icon=os.path.join("recursos", "imagem", "peixa.ico"))]
)