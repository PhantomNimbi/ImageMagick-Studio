' Windows Script Host - Zero Console Window Launcher
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """C:\Users\Joshu\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"" main.py", 0, False