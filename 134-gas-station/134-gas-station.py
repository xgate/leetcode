class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        s = g = 0
        for i in range(0, len(gas)):
            g += gas[i]-cost[i]
            if g < 0:
                s = i+1
                g = 0
        
        return s
