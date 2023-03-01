import os

# current working directory
cwd = os.getcwd()
# print(cwd)         # C:\Users\slaishet\PycharmProjects\Practise\OS



# Changing the current working directory
chd = os.chdir('../')
# print(chd)             # None
# print(os.getcwd())     # C:\Users\slaishet\PycharmProjects\Practise



# Creating a directory
directory = 'GeeksforGeeks'
parent_dir = r'C:\Users\slaishet\PycharmProjects\Practise\OS'     # 'r' is used for raw data.
path = os.path.join(parent_dir,directory)
# os.mkdir(path)

directory1 = "geeks"
path = os.path.join(parent_dir,directory1)
# os.mkdir(path,mode=0o666)


# make a directory

directory2 = "sai"
parent_dir = r'C:\Users\slaishet\PycharmProjects\Practise\GeeksforGeeks/Authors'
path = os.path.join(parent_dir,directory2)

# os.makedirs(path)
# Directory 'GeeksForGeeks' and 'Authors' will be created too if it does not exists


# listing out files and directories with python
path = '/'
dir_list = os.listdir(path)
print(dir_list)

# Deleting Directory or Files using Python
# os.remove()
# os.rmdir()

"""
OSError in the case of invalid or inaccessible file names and paths, or other
 arguments that have the correct type, but are not accepted by the operating system. os.error is an alias for built-in OSError exception. 
"""

# os.popen()
"""
This method opens a pipe to or from command. The return value can be read or written depending on whether the mode is ‘r’ or ‘w’. 
"""

# os.close()

# import os
#
# fd = "GFG.txt"
# file = open(fd, 'r')
# text = file.read()
# print(text)
# os.close(file)

# os.remove(): Using the Os module we can remove a file in our system using the remove() method. To remove a file we need to pass the name of the file as a parameter.


# os.path.exists(): This method will check whether a file exists or not by passing the name of the file as a parameter.

import os

print(os.path.exists('os_module.py'))  # returns either True or False. Can be used in if else condition.

# os.path.getsize()
#  python will give us the size of the file in bytes.

print(os.path.getsize(os.getcwd()))














