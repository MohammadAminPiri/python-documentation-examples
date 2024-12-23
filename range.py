# Write a program that generates a list of all even numbers between 10 and 30 using the range() function.


for i in range(10, 30):
    if i % 2 == 0:
        print(i)
    else:
        continue
