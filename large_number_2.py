a = int(input("Enter your first number....")) 
b = int(input("Enter your second number....")) 
c = int(input("Enter your third number....")) 

print()
if a>b and a>c:
    print("This is the larger number..", a)
elif b>a and b>c:
    print("This is the larger number..", b)
else:
    print("This is the larger number..", c)
 