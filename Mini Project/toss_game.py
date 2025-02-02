import random as r

choice=["head","tail"]
toss=r.choice(choice)

count=3
captain1=input("Do you want the head ? ").lower()
captain2=input("Do you want tail  ? ").lower()
print("Out of 3 will be Toss winning Best of Luck :)")
while count>0:
  count-=1
  if toss=="head" and captain1=="yes":
   print("its head you win the toss")
   
  elif toss=="head" and captain2=="yes":
    print("its tail you win the toss")
    
  else:
    print("its draw")
  

   
  
