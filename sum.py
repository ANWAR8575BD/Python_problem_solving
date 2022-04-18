lower = int(input("Enter your first input...."))
upper = int(input("Enter your second input...."))
result = 0

for num in range(lower, upper + 1):
    if num % 7 ==0:
        result = result + num
print(result)
    
        
