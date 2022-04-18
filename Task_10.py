"""Arrange string characters such that lowercase letters should come first\n str = AnWaR"""
print(__doc__)

str = "AnWaR"
lower = []
uper = []

for j in str:
    if j.islower():
        lower.append(j)
    else:
        uper.append(j)

Result = ''.join(lower + uper)
print("Expected Output: ",Result)