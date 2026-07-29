class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d=""
        d="".join(sorted(s[:len(s)//2]))

        return d+s[len(s)//2]+d[::-1]  if len(s)%2!=0 else d+d[::-1]