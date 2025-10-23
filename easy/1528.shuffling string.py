class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
       
        a = [''] * len(s)
  
        for i in range(len(s)):
            a[indices[i]] = s[i]
        
  
        return ''.join(a)
