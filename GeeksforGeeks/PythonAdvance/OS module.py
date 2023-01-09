import os
cwd = os.getcwd()

print("Current working directory :",cwd)

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

# printing cwd
current_path()

# changing the cwd
os.chdir('../')

# printing cwd
current_path()

# Creating a directory
directory = "GeeksforGeeks"
parent_dir = "D:/Pycharm projects/"

path = os.path.join(parent_dir,directory)
os.mkdir(path)
print("Directory '% s' created " %directory)

directory = "Geeks"

parent_dir = "D:/Pycharm projects"

mode = 0o666

path = os.path.join