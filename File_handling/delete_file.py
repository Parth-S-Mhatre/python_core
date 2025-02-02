import os
import shutil
path="Empty"
try:
    #os.remove(path) # delete the file
   # os.rmdir(path) #delete the folder
    shutil.rmtree(path)# delete the folder containing files
except FileNotFoundError:
    print("The file /folder does not exist")
except PermissionError:
    print("You do not have permission to delet the file/folder")
except OSError:
    print("You can't delete that folder using os.rmdir ")
else:
    print(f"The file /folder {path} has deleted")