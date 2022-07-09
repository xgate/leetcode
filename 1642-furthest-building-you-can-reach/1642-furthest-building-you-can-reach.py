from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:        
        
        if len(heights) == 1:
            return 0
        
        b, q = 0, PriorityQueue()
        
        for i in range(1, len(heights)):
            diff = heights[i]-heights[i-1]
            if diff > 0:
                if ladders > 0:
                    q.put(diff)
                    if q.qsize() > ladders:
                        b += q.get()
                else:
                    b += diff
                        
            if b > bricks:
                return i-1
        
        return len(heights)-1
    