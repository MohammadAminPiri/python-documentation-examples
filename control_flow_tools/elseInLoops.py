"""
else Clauses in Loops

Write a function to check if a given number is prime. Use a for loop with an else clause.
"""


def is_prime(n):
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisors from 2 to sqrt(n)
        if n % i == 0:  # If divisible, it's not prime
            return False
    else:
        # This `else` runs if the loop completes without finding a divisor
        return True


print(is_prime(2))
print(is_prime(4))
print(is_prime(7))
print(is_prime(15))
