from cx_Freeze import setup, Executable

base = None

executables = [
    Executable('automate_git.py', base=base)
]

setup(
    name="TaoBao",
    version="1.0",
    description="http://blog.csdn.net/u012175089",
    executables=executables, requires=['cx_Freeze']
)
