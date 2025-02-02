import random
def spin_row():
    row=["🍉","🍋","🔔","⭐","🍎"]

    return[random.choice(row) for _ in range(3)]

def print_row(row):
    print("🎊🎊🎊🎊🎊🎊🎊")
    print(" | ".join(row))
    print("🎊🎊🎊🎊🎊🎊🎊")

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0]=='🍉':
           return bet*3
        if row[0]=='🍋':
            return bet*3
        if row[0]=='🔔':
            return bet*7
        if row[0]=='⭐':
            return bet*15
        if row[0]=='🍎':
            return bet*10
        
    return 0
        
balance=0

print("  ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨  ")
print("✨  Welcome to the Diamond Casino & Resort  ✨")
print("  ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨   ")
print()


try:
    balance=int(input("Enter your balance:"))
except ValueError as e:
    print("Enter Numeric value plz :(")
else:
    print(f"Your balance is ${balance}")

if balance<0:
    print("Negative Number is not allowed")
while balance>0:
    bet=int(input("Enter your bet amount: "))
    if bet<0:
     print("Negative Number is not allowed")
    elif bet>balance:
        print("Insufficient balance :(")
    else:
        balance-=bet
        print("💫💫💫💫💫💫💫💫💫💫")
        print("   Symbols:🍉🍋🔔⭐🍎  ")
        print("💫💫💫💫💫💫💫💫💫💫")
        print()
        row=spin_row()
        print("🎇🎇🎇🎇Spinnning🎇🎇🎇🎇\n")
        print_row(row)
        print(f"Your balance left:${balance}")
  
        pay=payout(row,bet)
        if pay>0:
            print(f"You won ^_^ ${pay}")
        else:
            print("You lose this round ＞﹏＜")
        balance+=pay
        
        playagain=input("Do you want to play again ?(Yes or No):").lower()
        if playagain!="yes":
            break

print ("😵‍💫Game Over 😵‍💫")
print(f"Your Final balance is ${balance}")

