#To print all prime number between 15 to 45
print("All prime number between 15 to 45")
for a in range(15,46):
    for i in range(2,a):
        if a%i==0:
            break
    else:
        print("Prime =",a)

# To print given number is prime or not
print("Enter any element")
n=int(input())
flag=False
for e in range(1,n+1):
    for i in range(2,e):
        if(e%i==0):
            flag=True
            break
    
            
