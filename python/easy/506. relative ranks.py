class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x=[]
        for i in range(len(score)):
            v= sorted(score,reverse=True).index(score[i])
            if v>2:
                x.append(str(v+1))
            if v==0:
                x.append("Gold Medal")
            elif v==1:
                x.append("Silver Medal")
            elif v==2:
                x.append("Bronze Medal")
        return x
