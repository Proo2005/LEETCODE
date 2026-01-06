class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiouAEIOU'
        
        is_alnum = word.isalnum()
        alpha_count = sum(c.isalpha() for c in word)
        digit_count = sum(c.isdigit() for c in word)
        has_vowel = any(c in vowels for c in word)
        has_consonant = any(c.isalpha() and c not in vowels for c in word)

        return (
            is_alnum and has_vowel and has_consonant and (
                alpha_count >= 3 or
                (alpha_count >= 2 and digit_count >= 1)
            )
        )
