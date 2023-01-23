print("Enter three number for length of a triangle")
a,b,c=int(input()),int(input()),int(input())
print("press 1 to check isosceles triangle")
print("press 2 to check Right angle triangle")
print("press 3 to check equilateral triangle")
print("press 4 for exit")
n=int(input())
match n:
    case 1:
        if(a==b or b==c or c==a):
            print("Isosceles triangle")
        else:
            print("not isosceles triangle")
    case 2:
        if(c**2==b**2+a**2 or b**2==c**2+a**2 or a**2==b**2+c**2):
            print("Right angle triangle")
        else:
            print("not right angle triangle")
    case 3:
        if(a==b or b==c or c==a):
            print("Equilateral triangle")
        else:
            print("not equilateral triangle")
    case 4:
        print("Good bye...!")
    case _:
        print("invalid choice")