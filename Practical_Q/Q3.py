list=[]
n=int(input("Enter the Number of the element:"))
for i in range(n):
    list.append(int(input("Enter the Number:")))

print("Before list:",list)
while 1:
    print("~~~~~~List Operations~~~~~~")
    print("1)Even or odd list")
    print("2)Sort the list and merge")
    print("3)MAx elemnt from list")
    print("4)Min element from list")
    print("5)Exit")

    choice=int(input("Enter the choice"))
    
    if choice==1:
        even=[x for x in list if x%2==0 ]
        odd=[x for x in list if x%2!=0]
    print("Printing the Even Element=",even)
    print("Printing the Odd Element=",odd)
    if choice==2:
        even.sort()
        odd.sort()
        mergelist=[]
        mergelist=even+odd
    print("Sorted list ",mergelist)
    if choice==3:
        print("Maxmium element in a lisr",max(list))
    if choice==4:
        print("Maxmium element in a lisr",min(list))
    if choice==5:
        print("Exit the Program")
        break
    
    
        

    