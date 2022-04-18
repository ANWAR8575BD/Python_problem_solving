"""Given a list of numbers, Iterate it and print only those numbers which are divisible of 5\n"""
print(__doc__)

#n = int(input('Enter your input:... '))

for i in range(5):
    for j in range(i, -1, -1):
        print(i+1, end=" ")
    print()
