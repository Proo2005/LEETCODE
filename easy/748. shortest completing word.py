from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = ''.join([c.lower() for c in licensePlate if c.isalpha()])
        target_counter = Counter(target)

        res = None
        for word in words:
            word_counter = Counter(word)
   
            if all(word_counter[c] >= target_counter[c] for c in target_counter):
                if res is None or len(word) < len(res):
                    res = word    
        
        return res