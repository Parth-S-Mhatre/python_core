
name=input("What's your name ?").strip().title() # input command
print("hello",name)
print("hello ,"+name)
print("hello,",end="")#overiding sep,end parameter
print("parth")
print(f"hello, {name}")
#strings inbuilt function
#remove blank space from str
name=name.strip()
# to make first word capital
name=name.capitalize()
# to make every word capital
name=name.title()
#remove blank space and capital from str
name=name.strip().title()
#split user name into first name and last name
first,last=name.split(" ")
print(f"hello,{first}")
print(f"hello,{name}")
#functions
def hello(to="parth"):#default argument
    print("hello world, ",to)
  
hello()