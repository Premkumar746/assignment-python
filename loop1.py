'''sum1=0
for a in range(1,int(input("Enter no. of terms"))+1):
    sum1=sum1+a
print(sum1)

# To print sum of square of n natural number
sum=0
for a in range(1,int(input("Enter number of terms"))+1):
      sum=sum+a**2
print(sum)

# To print sum of cube of n natural number
sum=0
for a in range(1,int(input("Enter number of terms"))+1):
      sum=sum+a**3
print(sum)

#To print sum of n even natural number
sum=0
for a in range(1,int(input("Enter number of terms"))+1):
      sum=sum+a*2
print(sum)

#To print sum of n odd number
sum=0
for a in range(1,int(input("Enter number of terms"))*2):
      if(a%2!=0):
        sum=sum+a
print(sum)'''

#To print factorial of n number
import sys
n=int(input("Enter number to claculate factorial :-"))
f=1
for a in range(1,n+1):
    f=f*a
sys.set_int_max_str_digits(f) 
print("Factorial of ",n,"=",f)
