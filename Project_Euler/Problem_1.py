"""
Author: Giulio
Project Euler
"""

"""
Problem 1: Multiple of 3 and 5

If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6, and 9.  
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5
below 1000

"""

below = 10
numbers = [3, 5]

sum = 0

for i in range(1, below):
    if (i % numbers[0]) == 0:
        sum += i
    elif (i % numbers[1]) == 0:
        sum += i

print(f"The sum of the multiples of {numbers[0]} and {numbers[1]}\\n"
      f"below {below} is {sum}")