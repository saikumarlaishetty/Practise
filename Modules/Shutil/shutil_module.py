"""
Shutil module offers high-level operation on a file like a copy, create, and remote operation on the file.
"""

# Copying files to another directory

"""
shutil.copy() method in Python is used to copy the content of the source file to the destination file or directory. 
It also preserves the file’s permission mode but other metadata of the file like the file’s creation and modification times is not preserved.
The source must represent a file but the destination can be a file or a directory. If the destination is a directory 
then the file will be copied into the destination using the base filename from the source. Also, the destination must be writable. If the destination is a file and already exists then it will be replaced with the source file otherwise a new file will be created.

"""

import shutil
import os

# To get current file name
source = __file__


if not os.path.exists(os.path.join(os.getcwd(),"example")):
    os.mkdir(os.path.join(os.getcwd(),"example"))

destination = os.path.join(os.getcwd(),"example")

# copies the source to destination
dest = shutil.copy(source,destination)




