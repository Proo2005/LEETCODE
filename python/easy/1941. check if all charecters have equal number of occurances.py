class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return sorted(s)== sorted("".join(set(s))*(len(s)//len(set(s))))