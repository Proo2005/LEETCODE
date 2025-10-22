class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(s, openN, closeN):
           
            if len(s) == 2 * n:
                res.append(s)
                return
               # Add an open bracket if possible
            if openN < n:
                backtrack(s + "(", openN + 1, closeN)
            
        
            if closeN < openN:
                backtrack(s + ")", openN, closeN + 1)

        backtrack("", 0, 0)
        return res
