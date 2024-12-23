# Write a function that repeatedly divides a number by 2 until it becomes less than 1. Return the number of iterations it takes.


def count_iterations(x):
    count = 0
    while x > 1:
        x = x / 2
        count += 1
    print(count)


count_iterations(20)
