class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=[]
        for i in s1.split(" "):
            if s1.split(" ").count(i)==1 and i not in s2.split(" "):
                a.append(i)
        for i in s2.split(" "):
            if s2.split(" ").count(i)==1 and i not in s1.split(" "):
                a.append(i)        
        return a
