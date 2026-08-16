' Windows Script Host - Zero Console Window Launcher
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "python.exe main.py", 0, False