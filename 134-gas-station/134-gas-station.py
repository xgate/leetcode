class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s = prevGas = currentGas = 0
        n = len(gas)
        for i in range(0, n):
            currentGas += (gas[i] - cost[i])
            if currentGas < 0:
                s = i+1
                prevGas += currentGas
                currentGas = 0
        
        if currentGas+prevGas >=0:
            return s
        
        return -1
