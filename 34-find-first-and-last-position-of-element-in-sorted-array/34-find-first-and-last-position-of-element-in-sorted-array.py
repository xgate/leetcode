import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        return [-1 if l == len(nums) or nums[l] != target else l, -1 if r == 0 or nums[r-1] != target else r-1]
