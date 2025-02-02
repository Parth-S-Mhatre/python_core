x=int(input("Enter the 1st Number:"))
y=int(input("Enter the 2nd Number:"))
print("1)Addition")
print("2)subtraction")
choice=int(input("Enter the operations:"))
match choice:
    case 1:
        print(f"Addition of two Nums:{x+y}")
    case 2:
        print(f"Subtraction of two Nums:{x-y}")
    case _:
        print("Invalid choice!!!")#default like switch