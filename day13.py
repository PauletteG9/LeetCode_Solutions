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

# 3194. Minimum Average of Smallest and Largest Elements
"""You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even. You repeat the following procedure n / 2 times: Remove the smallest element, minElement, and the largest element maxElement, from nums. Add (minElement + maxElement) / 2 to averages. Return the minimum element in averages.
Difficulty: Easy
Approach: Brute Force"""

def minimumAverage(self, nums: list[int]) -> float:
    nums.sort()
    i=0
    j= len(nums)-1
    averages = []
    while i<j:
        averages.append((nums[i]+nums[j])/2)
        i+=1
        j-=1
    return min(averages)

# 2465. Number of Distinct Averages
"""You are given a 0-indexed integer array nums of even length. As long as nums is not empty, you must repetitively: Find the minimum number in nums and remove it. Find the maximum number in nums and remove it. Calculate the average of the two removed numbers. The average of two numbers a and b is (a + b) / 2. For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5. Return the number of distinct averages calculated using the above process. Note that when there is a tie for a minimum or maximum number, any can be removed.
Difficulty: Easy
Approach: Brute Force"""

def distinctAverages(self, nums: list[int]) -> int:
    nums.sort()
    i=0
    j = len(nums)-1
    averages = set()
    while i<j:
        average = nums[i]+nums[j]
        averages.add(average)
        i+=1
        j-=1
    return len(averages)