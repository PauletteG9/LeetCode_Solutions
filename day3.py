# 1351 : COUNT NEGATIVE NUMBERS IN A SORTED MATRIX
"""Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
Difficulty: Easy
Approach: Use Binary search to optimize finding the first negative number since the array is sorted."""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def find_first_negative_index(arr):
            low = 0
            high = len(arr) - 1
            first_neg_idx = len(arr) 

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] < 0:
                    first_neg_idx = mid  
                    high = mid - 1       
                else:
                    low = mid + 1       
                    
            return first_neg_idx
        
        total_negatives = 0
        for row in grid:
            idx = find_first_negative_index(row)
            total_negatives += len(row) - idx 
        
        return total_negatives