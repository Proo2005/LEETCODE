class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = s
        while len(c) > 2:  
            a = ''         
            for i in range(len(c) - 1):
                b = (int(c[i]) + int(c[i + 1])) % 10
                a += str(b)
            c = a

    
        return c[0] == c[1]