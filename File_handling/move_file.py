import os
soucre="Niceday.txt"
destination="C:\\Users\\parth\\OneDrive\Desktop\\Niceday.txt"
try:
 if os.path.exists(destination):
    print("File is already present")
 else:
    os.replace(soucre,destination)
    print(f"File is Moved {soucre}")
except FileNotFoundError:
  print("Oops unable to find the file :(")
