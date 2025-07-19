class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                if nums[mid] == target:
                    index = mid
            return index

        def findRight():
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                if nums[mid] == target:
                    index = mid
            return index

        return [findLeft(), findRight()]
                        
