# 462. Minimum Moves to Equal Array Elements II
"""Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal. In one move, you can increment or decrement an element of the array by 1. Test cases are designed so that the answer will fit in a 32-bit integer.
Difficulty: Medium
Approach: Min would be all the elements be the median of the array"""

def minMoves2(self, nums: List[int]) -> int:
  nums.sort()
  median = nums[len(nums)//2]
  count = 0
  for num in nums:
      count += abs(median-num)
  
  return count