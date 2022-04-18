"""Below are the two lists convert it into the dictionary\n keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]\n"""
print(__doc__)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

convert_dictionary = {}

for i in range(len(keys)):
    convert_dictionary[keys[i]] = values[i]

print("The dictionary is: ",convert_dictionary)