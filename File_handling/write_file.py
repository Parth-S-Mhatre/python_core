with open("Niceday.txt","w") as file:  # this will overwrite the given the file 
    file.write("Today is nice day")

with open("Niceday.txt","a") as file: # this will add the new content to the file
    file.write("\nI am happy")
