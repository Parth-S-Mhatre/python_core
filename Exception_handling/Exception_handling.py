try:
  numo=int(input("Enter the first Number:"))
  demo=int(input("Enter the second Number:"))
  result=numo/demo

except ZeroDivisionError as e:
  print(e)
  print("U can't Divde any Number by Zero U gandu")
except ValueError as e:
  print(e)
  print("Plz Enter Numeric Value")
except Exception as e:
  print(e)
  print("Something went wrong")
else:
  print(f"Result ={result}")
finally:
  print("Thank you !!!")  
  