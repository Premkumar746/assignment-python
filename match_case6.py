s=input("Enter any string :-")
match s:
    case s if ' ' in s:
        print("Multiword string")
    case s if ' ' not in s:
        print("Single word string")
print()
 
