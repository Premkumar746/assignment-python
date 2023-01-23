#  To sum each digit of given number
n=int(input("Enter any element"))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n//=10
print("Summation of each digit=",sum)