class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        def add_odd_indices(n, a):
            lst = list(n)
            for i in range(1, len(lst), 2):  
                lst[i] = str((int(lst[i]) + a) % 10)
            return "".join(lst)

        seen = set()
        small = s
        stack = [s]

        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)

      
            if cur < small:
                small = cur

       
            added = add_odd_indices(cur, a)

        
            rotated = cur[-b:] + cur[:-b]

      
            stack.append(added)
            stack.append(rotated)

        return small
