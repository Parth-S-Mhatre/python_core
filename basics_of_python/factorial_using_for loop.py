term=int(input("Enter the term:"))
if term<0:
    print("factorial of negative Number is not possible")
elif term ==0 and term ==1:
    print("factorial of term is 1")
else:
    fact=1
    for i in range(1,term+1): # range medhe starting and end point deicha asto like integration medhe kasa fakt end point
    # exclusive asto means 1 to 10 tr 1..9 pariyant jail manun term+1 kela like jr term asta tr 4 factorial pariyant gela asta
    #  u can try it by modifying the code range(1,term) and see the output
    # zero pasun ka ny start kela zero multiple by anything is zero
    # fact=1 that number will print means 5 factorial then is 5 which is error so baher value assign karichi
    # apn fact 1 ka ghetla because toh nanter change hot rahil tya mule fact baher thev for loop chya
     fact*=i

print("factorial of the term is",fact)