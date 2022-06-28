class Solution:
    
    def check(self, nums, ignore):
        del nums[ignore]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False
        return True
    
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        index = -1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                index = i-1
                break
        
        if index == -1:
            return True
        
        if self.check(nums.copy(), index):
            return True
        else:
            return self.check(nums.copy(), index+1)
