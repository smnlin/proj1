from shutil import copyfile, copyfileobj
from sys import exit
import os
import shutil

source = "/Users/simon/pyproj/proj1/binding.mp4"
target = "/Users/simon/pyproj/proj1/binding-copyfileobj.mp4"

try:
    #copyfile(source, target) #read the entire file in one go by default, copy only the data
    #shutil.copy(source, target) #copy with permissions
    shutil.copyfileobj(source, target)
except IOError as err:
    print(f"Unable to copy file {source} due to error {err}")
    exit(1)
except:
    print(f"Unexpected error: {Error}")
    exit(1)
print("File copy done")
