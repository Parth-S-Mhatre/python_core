item=input("What item you would like to add to your cart ? ")
price=float(input("Enter the price of the item: "))
quantity=int(input("How many you would like to buy: "))
bill=price*quantity
print(f"You have buy the item:{item} x {quantity}")
print(f"Your total bill is ${bill}")