from queue import PriorityQueue

class Solution:
    def canReach(self, heights, nth, bricks, ladders):
        b, q = 0, PriorityQueue()
        for i in range(1, nth+1):
            diff = heights[i]-heights[i-1]
            if diff > 0:
                q.put(-diff)
                b += diff
        
        if bricks >= b or ladders >= q.qsize():
            return True
        
        for i in range(ladders):
            q.get()
        
        while not q.empty():
            bricks -= (-q.get())
            if bricks < 0:
                return False
        
        return True

    
    # O(logN*(2N+N*logN))
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0
        
        if self.canReach(heights, len(heights)-1, bricks, ladders):
            return len(heights)-1
        
        l, r = 0, len(heights)-1
        while l <= r:
            m = int((l+r)/2)
            if self.canReach(heights, m, bricks, ladders):
                l = m+1
            else:
                r = m-1
        
        return r if m > r else m
    