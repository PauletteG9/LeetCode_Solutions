# 191. Number of 1 Bits
"""Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
Difficulty: Easy
Approach: Brute Force"""

def hammingWeight(self, n: int) -> int:
    if n == 0:
        return 0
    count = 0
    while n>0:
        if n%2 == 1:
            count += 1
        n//=2
    return count