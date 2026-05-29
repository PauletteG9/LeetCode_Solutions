# 3300. Minimum Element After Replacement With Digit Sum
"""You are given an integer array nums. You replace each element in nums with the sum of its digits.Return the minimum element in nums after all replacements.
Difficulty: Easy
Approach: Iterate over the array and for each element calcutate sum and append to new list and return"""

def minElement(self, nums: list[int]) -> int:
        sumOfDigits = []
        for num in nums:
            temp = num
            total = 0
            while temp>0:
                total += (temp%10)
                temp //= 10
            sumOfDigits.append(total)
        return min(sumOfDigits)
