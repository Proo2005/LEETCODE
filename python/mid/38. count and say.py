class Solution(object):
    def countAndSay(self, n):

        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = ""
        i = 0
        

        while i < len(prev):
            count = 1

            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                i += 1
                count += 1
            result += str(count) + prev[i]
            i += 1
        
        return result

        