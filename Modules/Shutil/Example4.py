"""
Replicating complete Directory

shutil.copytree() method recursively copies an entire directory
tree rooted at source (src) to the destination directory.
The destination directory,
named by (dst) must not already exist. It will be created during copying.

Syntax: shutil.copytree(src, dst, symlinks = False, ignore = None, copy_function = copy2, ignore_dangling_symlinks = False)

"""

# shutil.copytree(path,destination)


"""
Removing a Directory

shutil.rmtree() is used to delete an entire directory tree, 
the path must point to a directory (but not a symbolic link to a directory).

Syntax: shutil.rmtree(path, ignore_errors=False, onerror=None)


"""





"""
Finding files

shutil.which() method tells the path to an executable application that would be run if the given cmd was called. This 
method can be used to find a file on a computer which is present on the PATH.


"""
import shutil
import os

print(os.listdir())
print(os.getcwd())

cmd = "Example4.py"  # only executable application like .exe files run not other files.

print(shutil.which(cmd))


