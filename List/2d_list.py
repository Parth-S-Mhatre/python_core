import time as t
veg=["paneer masala","aloo masala","paneer kadai"]
non_veg=["Butter Chicken","mutton biryani","Anda curry"]
print("Vegetarian dishes:",veg)
print("Non-Vegetarian dishes:",non_veg)
menu=[veg,non_veg]
print("What would u like to order?")
order=input("Enter the category u want to order:")

if order=="veg":
    order1=int(input("In Veg menu what u would like to have:"))
    print(menu[0][order1])
    for second in range(3,0,-1):
        print(second)
        t.sleep(1)
    print("Order sucessfully :)")
else:
    order2=int(input("In Non-Veg menu what u would like to have:"))
    print(menu[1][order2])
    for second in range(3,0,-1):
        print(second)
        t.sleep(1)
    print("Order sucessfully :)")


feedback=input("Submit Experince with us:")
if feedback=="good":
    print("Thanks for your feedback")
else:
    print("Sorry to hear about that :(")
