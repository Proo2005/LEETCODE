class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left=[]
        equal=[]
        right=[]

        for x in nums:

            if x<pivot:
                left.append(x)

            elif x==pivot:
                equal.append(x)

            else:
                right.append(x)

        return left+equal+right