a=int(input("Enter a no:"))
b=int(input("Enter a no:"))
c=input("SELECT AN OpERATOR: A FOR ADD , S FOR SUBTRACT, M FOR MULTI, D FOR DIVISION\n")
if (c=="A"):
    d=a+b;
    print("Answer is :", d)
    
elif (c=="S"):
    d=a-b;
    print("Answer is :", d)
    
elif (c=="M"):
    d=a*b;
    print("Answer is :", d)

if (c=="D"):
    d=a/b;
    print("Answer is :", d)
