'''for a in range(1,10):
    print(5*a,end=' ')
print()

n=int(input("Enter any number"))
for i in range(1,11):
    print(n*i)
print()

n=int(input("Enter any number"))
for i in range(1,1+int(input("Enter number of terms"))):
    print(n*i)
print()
# print multiple of n in reverse
n=int(input("Enter any number"))
for i in range(11,0,-1):
    print(n*i)
print()
# print table user's choice
n=int(input("Enter number to print table"))
for i in range(1,11):
    print(n*i)
print()

#To print first n even natural number
for i in range(1,int(input("Enter number of terms"))*2+1):
    if(i%2==0):
       print(i)
print()

# To print n odd number
for i in range(1,int(input("Enter number of terms"))*2+1):
    if(i%2!=0):
       print(i)
print()

#To print square of n natural number
for a in range(1,int(input("Enter number of terms"))+1):
    print(a**2)
print()

# To print cube of n natural number
for a in range(1,int(input("Enter number of terms"))+1):
    print(a**3)
print()'''

# To print prime number within range of start=15 ,end=45
for a in range(15,46):
    for i in range(2,a):
        if(a%i==0):
            print("nothing")
        else:
            print(a)
