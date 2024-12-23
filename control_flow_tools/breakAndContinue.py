"""
break and continue Statements
Write a loop that iterates through numbers from 1 to 20 and prints:

"Fizz" if the number is divisible by 3.
"Buzz" if the number is divisible by 5.
Skips numbers divisible by both 3 and 5 without printing anything.
"""

i = 0
while i <= 20:
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0:
        print("Fizz", i)
    elif i % 5 == 0:
        print("Buzz", i)


# Break
# The break statement breaks out of the innermost enclosing for or while loop:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
