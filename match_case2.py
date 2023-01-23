n=int(input("press 1 for Addition \n press 2 for Subtraction \n press 3 for Multiplication \n press 4 for Division \n press__"))
match n:
    case 1:
        print("Enter aby two number to add")
        a,b=int(input()),int(input())
        c=a+b
        print("After addition=",c)
    case 2:
        print("Enter any two number to subtract")
        a,b=int(input()),int(input())
        c=a-b
        print("After subtraction =",c)
    case 3:
        print("Enter any two number to multiply")
        a,b=int(input()),int(input())
        c=a*b
        print("After multiplication=",c)
    case 4:
     print("Enter any two number to divide")
     a,b=int(input()),int(input())
     c=a/b
     print("After division=",c)
 
