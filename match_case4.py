n=int(input("Enter your age :__"))
match n:
    case n if (n<=10):
        print("you are a kid")
    case n if(n<=20):
       print("you are a Teen")
    case n if(n<=60):
       print("Experienced person")
    case n if(n>60):
        print("Seniour citizen")
print()