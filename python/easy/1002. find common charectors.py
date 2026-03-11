from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for w in words[1:]:
            common &= Counter(w)

        result = []
        for char in common:
            result.extend([char] * common[char])

        return result