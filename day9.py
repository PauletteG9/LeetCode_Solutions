# 3701. Compute Alternating Sum
"""You are given an integer array nums. The alternating sum of nums is the value obtained by adding elements at even indices and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]... Return an integer denoting the alternating sum of nums.
Difficulty: Easy
Approach: Brute Force"""

def alternatingSum(self, nums: List[int]) -> int:
    total = 0
    for i in range(len(nums)):
        if i%2 == 0:
            total += nums[i]
        else:
            total -= nums[i]
    return total

# 3110. Score of a String
"""You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters. Return the score of s.
Difficulty: Easy
Approach: Brute Force"""

def scoreOfString(self, s: str) -> int:
    total = 0
    for i in range(1, len(s)):
        total += abs(ord(s[i-1]) - ord(s[i]))
    
    return total

# 1281. Subtract the Product and Sum of Digits of an Integer
"""Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Difficulty: Easy
Approach: Brute Force"""

def subtractProductAndSum(self, n: int) -> int:
    prod = 1
    total = 0
    while n>0:
        digit = n%10
        prod *= digit
        total += digit
        n //= 10
    return prod - total

# 1672. Richest Customer Wealth
"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has. A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
Difficulty: Easy
Approach: Brute Force"""

def maximumWealth(self, accounts: List[List[int]]) -> int:
    max_wealth = 0
    for account in accounts:
        max_wealth = max(max_wealth, sum(account))
    
    return max_wealth