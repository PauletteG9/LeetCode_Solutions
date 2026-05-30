# 35. Search Insert Position
"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
Difficulty: Easy
Approach: Brute force"""

def searchInsert(self, nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i]>target:
            return i
    return len(nums)

# 344. Reverse String
""" Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array in-place with O(1) extra memory.
Difficulty: Easy
Approach: Reversing just half of the data and since its inplace keep in mind whle just implementing the question"""

def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    for i in range(n//2):
        temp = s[i]
        s[i] = s[n-i-1]
        s[n-i-1] = temp

# 145. Binary Tree Postorder Traversal
"""Given the root of a binary tree, return the postorder traversal of its nodes' values.
Difficulty: Easy
Approach: PostOrder Traversal is Left Right Root"""

def postorderTraversal(self, root) -> list[int]:
        result = []
        
        def tree(node):
            if not node:
                return
            tree(node.left)
            tree(node.right)
            result.append(node.val)

        tree(root)    
        return result

# 1346. Check if N and its double exist
"""Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
Difficulty: Easy
Approach: Create a hashset for already seen elements Check for a condition that if number is even and half of that number if its there in the hash set"""

def checkIfExist(self, arr: list[int]) -> bool:
    seen = set()
    
    for num in arr:
        if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
        
    return False

# 1394. Find lucky integer in an array
"""Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value. Return the largest lucky integer in the array. If there is no lucky integer return -1.
Difficulty: Easy
Approach: Implement a frequency counter and then iterate over hashtable to find maximum."""

def findLucky(self, arr: list[int]) -> int:
    lucky = {}
    for num in arr:
        lucky[num] = lucky.get(num, 0) + 1
        
    lucky_count = -1
    for num in lucky:
        if lucky[num] == num:
            lucky_count = max(lucky_count, num)
    
    return lucky_count

# 1431. Kids with the greatest number of candies.
"""There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have. Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise. Note that multiple kids can have the greatest number of candies.
Difficulty: Easy
Approach: Brute Force"""

def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    max_candy = max(candies)
    result = []

    for candy in candies:
        if (candy + extraCandies) >= max_candy:
            result.append(True)
        else:
            result.append(False)
    
    return result

# 1491. Average Salary Excluding the Minimum and Maximum Salary
"""You are given an array of unique integers salary where salary[i] is the salary of the ith employee. Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
Difficulty: Easy
Approach: Brute force"""

def average(self, salary: list[int]) -> float:
    min_salary = min(salary)
    max_salary = max(salary)

    total_salary = sum(salary)

    return (total_salary - min_salary - max_salary)/(len(salary)-2)