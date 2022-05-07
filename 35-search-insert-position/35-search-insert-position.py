class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        m = 0
        
        if nums[0] > target: 
            return 0
        if nums[r] < target:
            return r + 1
        
        while l <= r:
            m = int((l+r)/2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        
        if nums[m] < target:
            return m + 1
        else:
            return m
