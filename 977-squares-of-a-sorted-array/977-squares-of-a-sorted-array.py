# [-4,-1,0,3,10]
# [16, 1,0,9,100]
#  <---| |--->
#    neg pos
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = -1
        for i in range(len(nums)):
            if nums[i] < 0: neg = i
        nums = [n*n for n in nums]
        if neg == -1:
            return nums
        pos = neg+1
        ans = list()
        while neg >= 0 and pos < len(nums):
            if nums[neg] > nums[pos]:
                ans.append(nums[pos])
                pos += 1
            else:
                ans.append(nums[neg])
                neg -= 1
        for i in range(pos, len(nums)):
            ans.append(nums[i])
        for i in range(neg, -1, -1):
            ans.append(nums[i])
        return ans
