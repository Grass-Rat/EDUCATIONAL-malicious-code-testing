Certainly! Here's the GitHub README formatted with descriptions for each program:

---

## One: Simple Virus in Python

This code represents a simple virus written in Python. It replicates itself by creating a new binary executable file with a randomly generated filename. The code achieves this by:

1. Importing necessary modules: `argv` from `sys`, `choice` and `randint` from `random`, and `ascii_letters` from `string`.
2. Defining a lambda function `Randstr` to generate a random filename with a specified length, appending ".exe" extension to it.
3. Generating a random filename using `Randstr` function with a length between 4 and 8 characters.
4. Retrieving the name of the current script.
5. Opening the current script file in binary read mode and reading its content.
6. Writing the read content into a new file with the generated random filename in binary write mode.

In summary, this code creates a copy of itself with a randomly generated filename ending with ".exe", effectively spreading as a virus.

## Two: DLL Injection in C++

This script attempts to inject a DLL named "injrcted.dll" into the "explorer.exe" process using the Windows API functions provided by `ctypes.windll.kernel32`. It first loads the DLL file, retrieves the process ID (PID) of the "explorer.exe" process, opens a handle to that process, allocates memory within it, writes the DLL file into the allocated memory, and finally creates a remote thread within the process to execute the DLL.

## Three: Worm Replication in C++

This code defines a class named `Worm`, which represents a worm-like malware capable of replicating itself and other files. It initializes with parameters such as path, target directories list, and iteration. The `list_directories` method recursively lists directories and files, excluding hidden files/directories, while `create_new_worm` method is intended to create a copy of the script in each target directory.

Overall, this code provides the foundation for a worm malware that can traverse directories and replicate itself, but it lacks the complete functionality.

## Four: Self-Replicating Program in C++

This C++ code represents a simple self-replicating program. It generates a random filename, reads the content of the current script file, creates a new file with the generated filename, and writes the script content into it. The generated filename has a random length between 4 and 8 characters, followed by the ".exe" extension.

## Five: Worm-like Program in C++

This C++ code defines a worm-like program capable of recursively listing directories, avoiding hidden files, and creating new copies of itself in each target directory. It utilizes the `<filesystem>` library introduced in C++17. The `Worm` class has methods to list directories and create new worm copies, while the `main` function initializes the program and starts the worm actions.

Overall, this code represents a self-replicating program capable of spreading itself by creating copies in multiple directories while avoiding hidden files/directories.

--- 

This README provides an overview of each program and its functionality.
