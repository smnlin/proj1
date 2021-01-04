from shutil import copyfile, copyfileobj, copy2
from sys import exit
import os
import shutil

source = "/Users/simon/pyproj/proj1/binding.mp4"
target = "/Users/simon/pyproj/proj1/binding-copy2.mp4"
fsrc = open(source, "r")
fdst = open(target, "w")
try:
    """
    1.
    copyfile(source, target) #read the entire file in one go by default, copy only the data
    2.
    shutil.copy(source, target) #copy with permissions
    3.
    with open(source, "rb") as f_in, open(target, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    """
    copy2(source, target)
except IOError as err:
    print(f"Unable to copy file {source} due to error {err}")
    exit(1)
except:
    print(f"Unexpected error")
    exit(1)
finally:
    fsrc.close()
    fdst.close()
print("File copy done")
