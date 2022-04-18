"""Print downward Half-Pyramid Pattern with Star (asterisk)\n"""
print(__doc__)

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()