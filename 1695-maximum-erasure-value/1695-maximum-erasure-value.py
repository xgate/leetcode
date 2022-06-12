class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        ss = set()
        l = r = ans = 0
        currSum = 0
        while r < len(nums):
            if nums[r] in ss:
                while nums[l] != nums[r]:
                    ss.remove(nums[l])
                    currSum -= nums[l]
                    l += 1
                currSum -= nums[l]
                l += 1          
            ss.add(nums[r])
            currSum += nums[r]
            ans = max(ans, currSum)
            r += 1            
        return ans
