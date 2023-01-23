colour=input("Enter your favourite colour")
print("I like",colour,"colour")
match colour:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case 'orange':
        print("Wednesday")
    case 'white':
        print("Thursday")
    case 'black':
        print("Friday")
    case 'red':
        print("Saturday")
    case _:
        print("Sunday")
print()
