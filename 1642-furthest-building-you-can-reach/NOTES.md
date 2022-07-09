### 명백한 사실

`i` 까지 가는데 차이가 많이 나는 건물일수록 사다리를 이용하는 것이 낫다. (greedy)

### 접근법 1. parametric search

이진 탐색을 하면서 `i` 까지 갈 수 있는지를 조사하는 방법이다. upper bound 를 찾으면 된다.

일단 어디까지 가는지를 알면, 도달하는지 여부를 따지는 것은 상대적으로 쉽다고 생각했다.

가장 높은 건물을 오를때 사다리를 이용하는 것이 나으므로, priority queue 를 이용해서 사다리를 이용할 높이를 저장해뒀다.

```
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

        # 여기 한 줄로 생사가 갈렸다. 턱걸이
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
```

### 접근법 2. just priority queue

priority queue 를 쓰고 생각해보니, 결국 중요한 것은 사다리 찬스를 쓰는 것, 그러면 몇 개의 벽돌을 아낄 수 있는지 여부였다.

매번 queue 를 순회하지않아도, queue 안에 있는 벽돌의 갯수를 파악하는 것이 가능해보였다.

queue 가 가득 찼는지 여부를 따지는 부분을 생각해보니, 그 다음 과정은 자연스레 풀렸다.

```
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
            if ladders > 0: # 사다리가 0 개이면, queue maxsize 가 제대로 역할을 하지못함
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
```
