# ref solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        # Find the meet point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
