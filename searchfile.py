import os
import shutil


root_path = '/Users/timopiechotta/code'

def find_dirs(dir_path):
    dirs = []
    obj = os.scandir(dir_path)
    for entry in obj:
    #if entry.is_dir() or entry.is_file():
        #print(entry.name)
        if entry.is_dir():
            dirs.append(os.path.join(dir_path, entry.name))
    return dirs
    obj.close()

dirs_level_1 = find_dirs(root_path)
dirs_level_2 = []
dirs_level_3 = []

for dir in dirs_level_1:
    dirs_level_2.extend(find_dirs(dir)) # extend instead of append, because append would add a list to the list

for dir in dirs_level_2:
    dirs_level_3.extend(find_dirs(dir)) # extend instead of append, because append would add a list to the list

file_paths = []
for dirname in dirs_level_3:
    for file in os.listdir(dirname):
        if file == 'test.txt':
            # print(os.path.join(dirname, file))
            file_paths.append(os.path.join(dirname, file))

print(file_paths)

for dst in file_paths:
    shutil.copyfile('test.txt', dst)







