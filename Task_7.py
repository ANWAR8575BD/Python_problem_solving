
"""Given a two list of numbers create a new list such that new list should contain 
  only odd numbers from the first list and even numbers from the second list.\n list_1 = [2,5,8,12,4,6,87,32,65]\n list_2 = [1,6,3,90,4,5,32,4]"""
print(__doc__)

list_1 = [2,5,8,12,4,6,87,32,65]
list_2 = [1,6,3,90,4,5,32,4]
list_3 = [i for i in list_1 if not i % 2] + [i for i in list_2 if i % 2]

print('list_3 is: ',list_3)
