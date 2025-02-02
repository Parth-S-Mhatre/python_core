list=[]
n=int(input("Enter the No of element :"))
for i in range(n):
    list.append(int(input("Enter the Number")))
while 1:
    print("MENU DRIVEN PROGRAM")
    print("1)UPDATE the first value with X value")
    print("2)delete the middle element in list")
    print("3)add N name into the list")
    print("4)Exit")

    choice=int(input("Enter the choice:"))
    if choice==1:
      
      X=int(input("Enter the value to be update:"))
      list[0]=X
      print(list)

    elif choice==2:
       
       mid=(0+n)//2
       list.remove(mid)
       print(list)

    elif choice==3:
       
       size=int(input("Enter the N name you want to list "))
       for i in range(size):
          list.append(input("Enter the Name:"))
          print(list)
        
    elif choice==4:
         print("Exit the program:")
         break
    else:
         print("Enter the valid choice:!!!")
   





if "python" in list:
             print("Python is Present")
else:
     print("python is Not present")
