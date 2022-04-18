doc = """\nGiven two integer numbers return their product. If the product is greater than 1000, then return their sum"""
print(doc, '\n')

number_1 = 30
number_2 = 40
product = number_1 * number_2

if product < 1000:
    print('Your Result: ',number_1,"*",number_2, "=",product, '\n')
else:
    product = number_1 + number_2
    print('Your Result: ',number_1,"+",number_2, "=",product, '\n')