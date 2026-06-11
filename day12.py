# 2942. Find Words Containing Character
"""You are given a 0-indexed array of strings words and a character x. Return an array of indices representing the words that contain the character x. Note that the returned array may be in any order.
Difficulty: Easy
Approach: Brute Force"""

def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        index_array = []

        for idx, word in enumerate(words):
            if x in word:
                index_array.append(idx)

        return index_array