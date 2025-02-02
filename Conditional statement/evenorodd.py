def main():
    x=int(input("Enter the Number:"))
    if is_even(x):
        print("Even Number")
    else:
        print("Odd Number")
    
   
   
   
def is_even(n):
        return (n % 2==0)
        
    
    
main()