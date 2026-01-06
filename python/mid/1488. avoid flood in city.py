from bisect import bisect_right

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        full = set()
        dry_days = []
        lastRain = {}
        res = [-1] * n

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                res[i] = 1 
            else:
                if lake in full:
                   
                    prev_day = lastRain[lake]
                    idx = bisect_right(dry_days, prev_day)
                    if idx == len(dry_days):
                        return []  
                    dry_day = dry_days.pop(idx)
                    res[dry_day] = lake
                full.add(lake)
                lastRain[lake] = i
        return res
