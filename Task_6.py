"""Reverse a given number and return true if it is the same as the original number\n"""
print(__doc__)
number =input("Enter your input:.... ")

reverse_number = number[::-1]
if number == reverse_number:
    print("Accepted (True)")
else:
    number != reverse_number
    print("NotAccepted (False)")

