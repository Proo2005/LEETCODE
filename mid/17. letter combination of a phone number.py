from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

    
        combination = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index: int, current: str):
            if index == len(digits):
                result.append(current)
                return

            letters = combination.get(digits[index], "")
            for letter in letters:
                backtrack(index + 1, current + letter)

        backtrack(0, "")  
        return result
