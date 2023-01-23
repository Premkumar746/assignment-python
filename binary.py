#To print binary equivalent of a decimal number
n=int(input("Enter any element"))
bin=0 
a=1
while n>0:
    r=n%2
    bin=bin+r*a
    a=a*10
    n//=2
print(bin)

# To print decimal of a binary equivalent
n=int(input("Enter any binary equivalent"))

while n>0:
    r=n%10

#To print octal number of given decimal number
n=int(input("Enter any number without 8 and 9"))
oct=0
a=1
while n>0:
    r=n%8
    if(r<8):
        oct=oct+r*a
        a=a*10
    n//=8
print("Octal number=",oct)