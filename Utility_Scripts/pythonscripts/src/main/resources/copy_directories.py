########################################
#This code is used to copy src directory contents to destination directory.
#usage ex :- copy_directories.py a/* b
#a is the source directory, b is the destination directory.
#######################################
#!/usr/bin/python
import shutil
from sys import argv
def main(src, dest):
    try:
        shutil.copy(src, dest)
    # Directories are same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
src= str(argv[1])
dest=str(argv[2])
main(src, dest)

