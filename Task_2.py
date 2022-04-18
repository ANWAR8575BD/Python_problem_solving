
"""Given a string, display only those characters which are present at an even index number.\n string = Anwar Hossain"""
print(__doc__)

string = "Anwar Hossain"

for i in range(len(string)):
    if i % 2 == 0:
        print(string[i], end="','")
    
print("\n Program is closed....")


