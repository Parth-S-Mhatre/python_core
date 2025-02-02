# remove the specific element
thislist=["apple","banana","cherry"]
thislist.remove("banana")     # duplicate element can be deleted at Once only
print(thislist)
thislist.pop(1)         # remove specific element from the list by the index usually removes the last element
# thislist.clear the whole list
for x in thislist:
    print(x)   # loop for list
    
[print(x) for x in thislist]
    
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#The Syntax
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  # print only a element containing
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 