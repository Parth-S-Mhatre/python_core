def show_balance():
  print(f"the balance is ₹{balance:.2f}")

def deposit():
 amount=float(input("Enter the amount to be deposited:"))
 if amount<0:
  print("Negative Number is not allowed")
  return 0
 else:
  print(f"Amount deposited =₹{amount}")
  return amount
  
def withdraw():
 if balance<=0:
  print("Insufficient Balance")
  return 0
 else:
  cash=float(input("Enter the amount to be withdraw:"))
  if cash>balance:
   print(f"Not possible as balance is{balance} ")
   return 0
  else:
   print(f"Cash withdraw amount:₹{cash}")
   return cash

balance=0
is_running=True

while is_running:
 print("*******Welcome to the SBI Bank of India******")
 print("1)show Balance")
 print("2)Deposit amount")
 print("3)Withdraw Cash ")
 print("4)Exit the appliaction")
 choice=int(input("Enter the choice:"))

 match choice:
  case 1:show_balance()
  case 2:balance+=deposit()
  case 3:balance-=withdraw()
  case 4:is_running=False
  case _:print("INVALID CHOICE!!!")



print("Thank you!! have a nice day")