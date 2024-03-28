One: 
This script attempts to inject a DLL named "injrcted.dll" into the "explorer.exe" process using the Windows API functions provided by ctypes.windll.kernel32. It first loads the DLL file, retrieves the process ID (PID) of the "explorer.exe" process, opens a handle to that process, allocates memory within it, writes the DLL file into the allocated memory, and finally creates a remote thread within the process to execute the DLL.

Two:

Three:

Four:

Five:
