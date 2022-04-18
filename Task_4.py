"""Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
\nlist_number = [2, 10, 20, 16, 15, 22, 25, 30, 3, 7, 9]"""
print(__doc__)

list_number = [2, 10, 20, 16, 15, 22, 25, 30, 3, 7, 9]
list = [n for n in list_number if not n % 5]
print(list)
    
    
