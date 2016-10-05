#!/usr/bin/python
import shutil, sys

def main(src, dest):
    try:
        shutil.copy(src, dest)
    # Directories are same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
src= str(sys.argv[1])
dest=str(sys.argv[2])
main(src, dest)

