class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
    # Extract vowels
        vowel_list = [c for c in s if c in vowels]
    # Sort by ASCII
        vowel_list.sort()
    
        result = []
        idx = 0
        for c in s:
            if c in vowels:
               result.append(vowel_list[idx])
               idx += 1
            else:
                result.append(c)
    
        return "".join(result)
        