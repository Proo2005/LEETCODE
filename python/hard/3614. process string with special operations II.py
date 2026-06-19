class Solution:
    def processStr(self, s: str, k: int) -> str:

        lengths = []
        curr_len = 0
        
        for char in s:
            if char.isalpha():  
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass  
            
            lengths.append(curr_len)

            if curr_len > k * 2 + 2:
          
                pass


        if not lengths or k < 0 or k >= lengths[-1]:
            return "."
    
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            
            if char == '#':
                prev_len = lengths[i] // 2
                if k >= prev_len:
                    k %= prev_len
            elif char == '%':
                curr_len = lengths[i]
                k = curr_len - 1 - k
            elif char == '*':
                pass
            else:
              
                prev_len = lengths[i] - 1
                if k == prev_len:
                    return char
                    
        return "."
