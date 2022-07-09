from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        if len(heights) == 1:
            return 0
        
        q = PriorityQueue(maxsize=ladders)
        totalBricks = bricksInQue = 0
        for i in range(1, len(heights)):
            diff = heights[i]-heights[i-1]
            if diff < 0:
                continue
            totalBricks += diff
            if ladders > 0:
                if q.full():
                    minDiff = q.get()
                    if diff > minDiff:
                        q.put(diff)
                        bricksInQue += (diff-minDiff)
                    else:
                        q.put(minDiff)
                else:
                    q.put(diff)
                    bricksInQue += diff
        
            if bricks < (totalBricks-bricksInQue):
                return i-1
        
        return len(heights)-1
    