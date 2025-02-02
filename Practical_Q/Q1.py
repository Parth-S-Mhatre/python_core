side=int(input("Enter the side of the square:"))
n=int(input("Enter the Number :"))
fact=1
if side<0 or n<0:
    print("Invalid Input!!!")
else:
    area=side**2
    perimenter=side*4
    for i in range(1, n+1):
     fact = fact * i
     
    print("Area of the Side",side," Square is",area)
    print("Perimeter of the Sidd ",side,"Square",perimenter)
    print("Factorial of the Number",n,"=",fact)