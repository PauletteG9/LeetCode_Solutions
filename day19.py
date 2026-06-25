# 3668. Restore Finishing Order
"""You are given an integer array order of length n and an integer array friends. order contains every integer from 1 to n exactly once, representing the IDs of the participants of a race in their finishing order. friends contains the IDs of your friends in the race sorted in strictly increasing order. Each ID in friends is guaranteed to appear in the order array. Return an array containing your friends' IDs in their finishing order.
Difficulty: Easy
Approach: simulation.
TC : O(n)
SC : O(n)"""

def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        friend_set = set(friends)
        return [num for num in order if num in friend_set]