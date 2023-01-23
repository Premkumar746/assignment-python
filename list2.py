'''#Write a Python script to find the smallest number in a given list of numbers.
l1=[23,45,34,65,76,56]
max=l1[0]
for x in l1:
    if max>x:
        max=x
print("smallest number=",max)

#write a Python script to calculate the sum of elements in a given list of numbers.
l1=[23,54,67,89,23]
sum=0
for x in l1:
    sum=sum+x
print("Summation=",sum)
    
print()'''

#Write a Python script to remove all non int values from a list
l1=[23,3.4,56,'a',45,2.6,3+6j]
print("Original elements are:")
print(l1)
for x in l1 :
    if x.isdecimal():
        print(l1)
