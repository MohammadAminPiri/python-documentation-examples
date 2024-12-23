"""
Write a function that takes a number as input and returns:

"Positive" if the number is greater than 0.
"Negative" if the number is less than 0.
"Zero" if the number is exactly 0.
"""

x = int(input("Please enter a integer: "))
if x < 0:
    print("Negative")
# Use elif whenever you want to have more than one if
elif x == 0:
    print("Zero")
else:
    print("Positive")
