class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = sorted(nums)[int(len(nums)/2)]
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i]-mid)
        return count
    