# ref discuss
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        currSum, sumNums = 0, sum(nums)
        l, maxLen = 0, -1
        for r in range(len(nums)):
            currSum += nums[r]
            while l <= r and currSum > sumNums - x:
                currSum -= nums[l]
                l += 1
            if currSum == sumNums - x:
                maxLen = max(maxLen, r-l+1)
        
        if maxLen == -1: 
            return -1
        
        return len(nums)-maxLen
    