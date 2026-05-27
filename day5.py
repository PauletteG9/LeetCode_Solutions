# 3121. Count the Number of Special Characters II
"""You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c. Return the number of special letters in word.
Difficulty: Medium
Approach: All the lowercase of the char should come before the first occurence of uppercase of the char so store the last occurence of lowercase and first occurence of uppercase and """

def numberOfSpecialChars(self, word: str) -> int:
        small = defaultdict()
        large = defaultdict()
        count = 0
        for index, char in enumerate(word):
            if char.islower():
                small[char] = index
            else:
                if char.lower() not in large:
                    large[char.lower()] = index
        for ch in small:
            if ch in large:
                if small[ch] < large[ch]:
                    count += 1
        return count