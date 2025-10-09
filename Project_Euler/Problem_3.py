"""
Author: Giulio
Project Euler
"""

"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5,7,13 and 29

Task:

What is the largest prime factor of the number
600851475143
"""

prime_factors = []
number = 13195

for i in range(2, number):
    # Check if i is a factor
    if number % i == 0:
        # Check if i is prime
        is_prime = True
        for j in range(2, i-1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_factors.append(i)
            
largest = max(prime_factors) 
print(largest)

