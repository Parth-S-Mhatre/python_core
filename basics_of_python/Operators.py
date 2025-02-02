#operators
# operators it is used in between two operands for ex addition ,subtraction and so on 
# type of operators
"""
1.Arithmetic operators-:
+ (addition):a+b
- (subtraction):a-b
* (multiplication):a*b
/(division):a/b
%(modulus):a%b remainder deto
**(raised to power):a**b ex 2**3=8
//(floor division):a//b without decimal value or removing points for ex-2.96 //2 not 3
2.Assignment operator-: nav medhech aahe assign karto value
= (equal to):a=b
+=(addition assignment):a+=b or a=a+b
-=(subtraction assignment):a-=b or a=a-b
*=(Multipliaction assignment):a*=b or a=a*b
/=(division assignment):a/=b or a=a/b
3.Comparsion Operator:
==(check if a is eqaul to b or not):a==b
!=(check if a is not eqaul to b or not):a!=b
>=(check if a is greater the b or eqaul to b or not):a>=b
>=(check if a is less the b or eqaul to b or not):a>=b
>(check if a is greater the b or not ):a>b
<(check if a is less the b or not ):a>b
Logical Operators:
and (check if both condition is true then only it is executed): a>10 and b<20
or (check if any condition is true then it is executed naytar doni false asel tr nay execute hoil):a>10 or b<20
not(jr utha condition asel like true asel tr fasle hoil ):not(a>10 and b<20)

"""
# Examples-: arimethic anni assignment tu kar evdha ky hard ny aahe
#we want to check whether it is even or odd
a=10
even=a%2  # 2 ne divide kela 10 tr remainder 0 yeil na
if even==0:
    print("it is even")

sum=0
sum=sum+5 # assignment operator (addition) ata sum chi value overlap hoil or rewrite u can say or reassign
print(sum)# output 5
# comparsion operator
parth=float(input("Enter the height:"))# my height is 5.85
jyoti=float(input("Enter the height:"))# ur height is 5.6
if parth>jyoti:
    print("parth is taller then you ")
# logical operator
# we want to check whether both person loves each other or not
pyupii=input("Enter the confession:")#  I love you Jyoti
jeff=input("Enter the confession:")#  love you too pyupii
# and operator
if pyupii=="I love you Jyoti" and jeff=="love you too pyupii":
    print(" we will marry in 2035")
# or operator
# we want to check whether konala cooking changli yete
parth1=input("Enter the cooking skill :")# i am good
jyoti1=input("Enter the cooking skill:")# i am descent 
if parth1=="i am good" or jyoti1=="i am good":
    print(" i am best at cooking ")

"""

Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y





"""