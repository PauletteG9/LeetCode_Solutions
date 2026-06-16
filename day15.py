# 3612. Process String with Special Operations I
"""You are given a string s consisting of lowercase English letters and the special characters: *, #, and %. Build a new string result by processing s according to the following rules from left to right: If the letter is a lowercase English letter append it to result. A '*' removes the last character from result, if it exists. A '#' duplicates the current result and appends it to itself. A '%' reverses the current result. Return the final string result after processing all characters in s.
Difficulty: Medium
Approach: Simulation"""

def processStr(self, s: str) -> str:
        result = ""
        for char in s:
            if char == '*':
                result = result[:-1]
            elif char == '#':
                result += result
            elif char == '%':
                result = result[::-1]
            else:
                result += char
        return result