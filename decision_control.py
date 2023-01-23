'''n=int(input("Enter any number"))
if n>0:
    print("Positive number")
elif n<0:
       print("Negative number")
else:
    print("Neutral")'''
#Check inputed element is divisible by 5 or not
'''n=int(input("Enter any number"))
if(n%2==0):
    print("Given number is Even")
else:
    print("Not Even number")'''
#input two words and arrange in dictionary order
'''print("Enter any two words")
a,b=input(),input()
print("In dictionary order")
if(a>b):
    print(a)
else:
    print(b)'''
#check whether a given quadratic equation has 
# two real & distinct roots,real & equal roots or imaginary roots  
'''print("Enter value of a,b,c of a quadratic equation")
import math
a,b,c=int(input()),int(input()),int(input())
d=(b**2)-4*a*c
if(d>0):
    r1=(-b+math.sqrt(d)/(2*a))
    r2=b+math.sqrt(d)/(2*a)
    print("Roots are real and unequal ",r1," and",r2)
elif d==0:
    r1=-b/(2*a)
    print("Roots are real and same ",r1)
else:
    print("No real roots are there")'''

#leap year or not
'''n=int(input("enter any year"))
if(n%4==0):
    print("Leap year")
else:
    print("Not leap")'''

#Check greater among three number
'''print("Enter any three number")
a,b,c=int(input()),int(input()),int(input())
if(a>b>c):
      print(a)
elif (b>c >a):
    print(b)
else:
    print(c)'''

#Input month in numeric form and print its days
n=int(input("Enter month value in numeric form"))
if(n==1,3,5,7,8 ,10 ,12):
    print("31 days")
elif(n==4,6,9,11):
    print("30 days")
else:
    print("28/29")


#[x for x in sorted(input("Enter any three String With comma").split(',')) if(print(x,end=' '))]