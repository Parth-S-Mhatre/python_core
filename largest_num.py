a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if a>b:
    if a>c:
        print("A",c," is greater than B and C")
if b>a:
    if b>c:
        print("B",c," is greater than A and C")
if c>a:
    if c>b:
        print("C",c," is greater than B and C")