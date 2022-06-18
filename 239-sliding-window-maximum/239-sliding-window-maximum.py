import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        heap = list()
        ans = list()        
        # first window
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        ans.append(-heap[0][0])
        # sliding window
        l = 0
        for r in range(k, len(nums)):
            l += 1
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
