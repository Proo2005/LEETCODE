class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_s=0
        for i in range(len(s)):
            ss=[]
            for j in range(i,len(s)):
                if s[j] not in ss:
                    ss.append(s[j])
                else:
                    break
            max_s=max(max_s,len(ss))
        return max_s