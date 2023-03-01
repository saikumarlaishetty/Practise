# copying the metadata along with file

"""
shutil.copy2()- This method is identical
 to shutil.copy() method but it also tries to preserve the file’s metadata.

"""
import os
import shutil

source = __file__
print(os.stat(source))

destination = 'check.txt'

dest = shutil.copy2(source,destination)
print(dest)

