import random as r

num=r.randint(5,10)
num2=r.random()
print(num2)

hand_game=["rock","paper","Scissors"]
z=r.choice(hand_game)
print(z)
cards=[1,2,3,4,5,6,7,8,9,"jack","Queen","King","Ace"]
r.shuffle(cards)
print(cards)
print(num)