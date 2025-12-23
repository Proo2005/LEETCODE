class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort(key=lambda x: x[0])
        
   
        ends = sorted(events, key=lambda x: x[1])
        
        ans = 0
        best = 0
        j = 0
        
        for start, end, value in events:
           
            while j < len(ends) and ends[j][1] < start:
                best = max(best, ends[j][2])
                j += 1
            
        
            ans = max(ans, best + value)
        
        return ans
