# 961. N-Repeated Element in Size 2N Array
"""You are given an integer array nums with the following properties: nums.length == 2 * n. nums contains n + 1 unique values, n of which occur exactly once in the array. Exactly one element of nums is repeated n times. Return the element that is repeated n times.
Difficulty: Easy
Approach: Hash set, just find num that occurs twice, since all other nums occur once.
TC : O(n)
SC : O(n)"""
 
def repeatedNTimes(self, nums: list[int]) -> int:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) +1
        if freq[num] > 1:
            return num

# 3866. First Unique Even Element
"""You are given an integer array nums. Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums. If no such integer exists, return -1.
Difficulty: Easy
Approach: Hash set.
TC : O(n)
SC : O(n)"""

def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0)+1
        
        for num, count in freq.items():
            if count == 1 and num%2 == 0:
                return num
            
        return -1