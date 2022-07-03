# 1) 모든 박스를 싣는다.
# 2) truckSize 에 맞을때까지, 가벼운 박스를 내린다.
from queue import PriorityQueue

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = units = 0
        que = PriorityQueue()
        for i in range(len(boxTypes)):
            boxes += boxTypes[i][0]
            units += (boxTypes[i][0] * boxTypes[i][1])
            que.put((boxTypes[i][1], boxTypes[i][0]))
        
        while boxes > truckSize:
            unit, box = que.get()
            if boxes - box >= truckSize:
                boxes -= box
                units -= (box * unit)
            else:
                units -= (unit * (boxes-truckSize))
                boxes = truckSize
        
        return units
