"""
Problem_1: Smallest Missing Positive Integer
Given an array A of N integers, return the smallest positive integer (greater than 0)
that does not occur in A.

Examples:

A = [1, 3, 6, 4, 1, 2] → 5
A = [1, 2, 3] → 4
A = [-1, -3] → 1

Constraints:
1 ≤ N ≤ 100,000
Each A[i] is in the range [-1,000,000 .. 1,000,000]
"""

def solution(A):
    
    n = 1

    if 1 not in A:
        return n
    
    A = sorted(A)
    if any((i < -1000000 or i > 1000000) for i in A):
       return print("Values has to be in the range [-1,000,000 - 1,000,000]")
    
    for i in A:
        v = n + i
        if v not in A and v > 0:
            return v

# Execution
     
A = [1,2,300,-1000,200000,400,3]
value = solution(A)
print(value)