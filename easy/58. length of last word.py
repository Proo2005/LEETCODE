class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[len(s.split())-1])
