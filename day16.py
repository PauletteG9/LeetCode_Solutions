# 3099. Harshad Number
"""An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.
Difficulty: Easy
Approach: Simulation"""

def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
    temp = x
    sumOfDigits = 0
    while temp>0:
        sumOfDigits += temp%10
        temp //= 10
    if x%sumOfDigits == 0:
        return sumOfDigits
    return -1