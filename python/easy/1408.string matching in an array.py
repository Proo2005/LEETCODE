class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=[]
        for i in words:
            
            for j in words:
                if j in i and j!=i and j not in a:
                    a.append(j)

        return a