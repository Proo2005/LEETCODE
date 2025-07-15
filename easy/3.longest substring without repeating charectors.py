class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        d = ''
        for i in s:
            if i not in d:
                d += i
            else:
                d = d[d.index(i)+1:] + i 
            max_len = max(max_len, len(d))
        return max_len

