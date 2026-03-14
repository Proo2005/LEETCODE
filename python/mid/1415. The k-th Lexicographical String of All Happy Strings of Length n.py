class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(curr):
            if len(curr) == n:
                res.append("".join(curr))
                return
            
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    curr.append(ch)
                    backtrack(curr)
                    curr.pop()

        backtrack([])

        if k > len(res):
            return ""
        
        return res[k-1]