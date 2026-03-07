class Solution:
    def wordPattern(self, s: str, t: str) -> bool:
        words = t.split()
        
        if len(s) != len(words):
            return False

        s_map = {}
        t_map = {}

        for char_s, word in zip(s, words):

            if char_s in s_map:
                if s_map[char_s] != word:
                    return False
            else:
                s_map[char_s] = word

            if word in t_map:
                if t_map[word] != char_s:
                    return False
            else:
                t_map[word] = char_s

        return True