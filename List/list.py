n=int(input("Enter the No of item:"))
cart=[]
count=0
for i in range(n):
    a=input("Add to card:") # insertion at the list
    cart.append(a) 
    
    
c=input("Do you want to replace item purschase:\nClick\nYes\nNo\n")  # amazon type functions
if c =="Yes":
    b=input("Enter the item to be replaced:")
    if b in cart:
     count=count+1
     cart[count]= a=input("Add to card the replace item:")   # updating an element
else:
    print("Thank you for shopping :)")
   
   
  
print("Your shopping list:",cart)
       
   
   
