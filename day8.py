# 3945. Digit Frequency Score
"""You are given an integer n. The score of n is defined as the sum of d * freq(d) over all distinct digits d, where freq(d) denotes the number of times the digit d appears in n. Return an integer denoting the score of n.
Difficulty: Easy
Approach: Brute force"""

def digitFrequencyScore(self, n: int) -> int:
        score = 0
        while n>0:
            score += n%10
            n //= 10
        return score

# 3940. Limit Occurrences in Sorted Array
"""You are given a sorted integer array nums and an integer k. Return an array such that each distinct element appears at most k times, while preserving the relative order of the elements in nums. Note: If a distinct element appears at least k times, then it must appear exactly k times in the resulting array.
Difficulty: Easy
Approach: Brute force"""

def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0)+1
            if freq[num]<=k:
                result.append(num)
        return result

# 3925. Concatenate Array With Reverse
"""You are given an integer array nums of length n. Construct a new array ans of length 2 * n such that the first n elements are the same as nums, and the next n elements are the elements of nums in reverse order. Formally, for 0 <= i <= n - 1:
ans[i] = nums[i], ans[i + n] = nums[n - i - 1]. Return an integer array ans.
Difficulty: Easy
Approach: Brute force"""

def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[n-i-1])
        return nums

# 3921. Score Validator
"""You are given a string array events. Initially, score = 0 and counter = 0. Each element in events is one of the following: "0", "1", "2", "3", "4", "6": Add that value to the total score, "W": Increase the counter by 1. No score is added, "WD": Add 1 to the total score, "NB": Add 1 to the total score.
Process the array from left to right. Stop processing when either: All elements in events have been processed, or The counter becomes 10. Return an integer array [score, counter], where: score is the final total score, counter is the final counter value.
Difficulty: Easy
Approach: Brute Force"""

def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for event in events:
            if counter == 10:
                return [score, counter]
            if event == "WD" or event == "NB":
                score += 1
            elif event == "W":
                counter += 1
            else:
                score += int(event)
        return [score, counter]