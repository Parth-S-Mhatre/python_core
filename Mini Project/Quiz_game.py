
questions=("1)Which of the following is an output device",
           "2)Which of the following is an input device",
           "3)which of the following is used to store data in a computer",
           "4)Which of the following is referred to as brain of a computer")

options=(("1.Keyboard","2.Joy stick","3.Printer","4.None of the above"),
         ("1.Moniter","2.Mouse","3.Hard disk","4.Printer"),
         ("1.Hard disk","2.CPU","3.Mointer","4.None of the above"),
         ("1.Ram","2.Rom","3.Mointer","4.CPU"))

answers=("3","2","1","4")
gusses=[]
score=0
question_no=0
for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_no]:
     print(option)
    guess=input("Enter (1,2,3,4) : ").upper()
    gusses.append(guess)
    if guess==answers[question_no]:
       score+=1
       print("CORRECT!")
    else:
       print("INCORRECT!!")
       print(f"CORRECT ANS IS {answers[question_no]}")
    question_no+=1


print("~~~~~~~~~~~~~~~~~~~")
print("      RESULT       ")
print("~~~~~~~~~~~~~~~~~~~")

score=int(score/len(questions)*100)
if score==100:
   print(f"You have Score {score}")
   print("Your genius :)")
elif score==80:
   print(f"You have Score {score}")
   print("Your excellent :)")
elif score==50:
   print(f"You have Score {score}")
   print("Your well try :|")
else:
   print(f"You have Score {score}")
   print("Better luck next time  :(")
   

