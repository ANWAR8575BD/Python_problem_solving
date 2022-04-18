
"""Given a list of numbers, return True if first and last number of a list is same.\n"""
print(__doc__)

number = [10, 2, 3, 4, 5, 6, 10]

print('The length of this list: ',len(number))
first_number = print("first number: ",number[0])
last_number = print('last number',number[6])

if (number[0]) == (number[6]):
    print ('First and last number is same, so return: ',True)
else:
    print('First and last number is not same, so return: ',False)
