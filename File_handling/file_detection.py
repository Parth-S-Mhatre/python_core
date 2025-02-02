import os
path="C:\\Users\\parth\\OneDrive\\Desktop\\test.txt"

if os.path.exists(path):
    print("File exits")
    if os.path.isfile(path):
        print("File is a file")
    elif os.path.isdir(path):
        print("File is directory")
else:
    print("File is neither exits nor directory")