n=int(input("Enter any number"))
match n:
    case n if n%2==0 and n>0:
        print("Shaurabh Shukla")
    case n if n%2!=0 and n<0:
        print("Pratik Jain")
    case n if n%2!=0 and n>0:
        print("Aditya Chaudhary")
    case _:
        print("Invalid number")