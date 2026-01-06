import re
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(rf"[{re.escape(string.punctuation)}]", "", s)
        return s[::-1].replace(" ","").lower() == s.replace(" ","").lower()