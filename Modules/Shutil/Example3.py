# Copying the content of one file to another
"""

shutil.copyfile() method in Python is used to copy the content
of the source file to the destination file. The metadata of the file is not copied. Source and destination must represent a file and destination must be writable. If the destination already exists then
 it will be replaced with the source file otherwise a new file will be created.

"""


import shutil

source = __file__

destination = "main2.py"
dest = shutil.copyfile(source,destination)
