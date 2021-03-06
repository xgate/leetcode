### 명백한 사실

`i` 까지 가는데 높이 차이가 많이 나는 건물일수록 사다리를 이용하는 것이 낫다. (greedy)

### 접근법 1. parametric search

이진 탐색을 하면서 `i` 까지 갈 수 있는지를 조사하는 방법이다. upper bound 를 찾으면 된다.

일단 어디까지 가는지를 알면, 도달 가능한지 여부를 따지는 것은 상대적으로 쉽다고 생각했다.

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

가장 많은 차이를 사다리가 감당한다는 것만 보장하면 된다.

`O(NlogN)`

```
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
```

