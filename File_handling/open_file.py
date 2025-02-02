try:
 with open("C:\\Users\\parth\\OneDrive\\Desktop\\intro.txt") as file:
    data=file.read()
    print(data)
except FileNotFoundError:
  print("File not found :(")
  