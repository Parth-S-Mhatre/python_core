rows=int(input("Enter the row:"))
columns=int(input("Enter the column:"))
symbol=input("Enter any symbol:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
