#sets is an unordered collection of unique element ,no duplicate value

#set is mutable
divisions = {"A","B","C","E"} 
grade={"A","B","C","F"}
#grade.add("Z")
#grade.remove("A")
#grade.clear()
#grade.update(divisions)
#info=divisions.union(grade)
print(divisions.difference(grade))
print(divisions.intersection(grade))
#for x in info:
 #   print(x)