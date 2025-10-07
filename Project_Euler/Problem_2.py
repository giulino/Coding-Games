"""
Author: Giulio
Project Euler
"""

"""
Problem 2: Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 and 2. 
The first terms will be: 1,2,3,5,8,13,21,34,55

Task:

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
"""

import numpy as np

def fibonacci_sequence(max_number):

    if max_number <= 0:
        return []
    elif max_number == 1:
        return [1]
    else: 
        sequence = [1, 2]

        next_term = 0

        while next_term < max_number:
            next_term = sequence[-1] + sequence[-2]
            if next_term < max_number:
               sequence.append(next_term)
        return sequence

sequence = fibonacci_sequence(90)

even_values = 0

for i in np.array(sequence):
    if i % 2 == 0:
        even_values += i

print(even_values)






