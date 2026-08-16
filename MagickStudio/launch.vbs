' Windows Script Host - Zero Console Window Launcher
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """%LOCALAPPDATA%\Python\pythoncore-3.14-64\pythonw.exe"" main.py", 0, False