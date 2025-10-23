class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        b=0
        for i in range(1,32000):
            if i not in arr:
                b+=1
                if b==k:
                    return i
