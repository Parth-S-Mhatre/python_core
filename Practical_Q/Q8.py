num = int(input("Enter the Number: "))
temp = num
rev = 0

# Check if the number is negative
if num < 0:
    print("It is not a Palindrome Number")
else:
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

    if temp == rev:
        print("It is a Palindrome Number")
    else:
        print("It is not a Palindrome Number")