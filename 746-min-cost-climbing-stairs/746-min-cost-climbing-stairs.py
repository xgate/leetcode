class Solution:
    
    def climb(self, cost, i, mem):
        if i < 0:
            return 0
        mem[i] = mem[i] if i in mem else cost[i] + min(self.climb(cost, i-1, mem), self.climb(cost, i-2, mem))
        return mem[i]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        return self.climb(cost, len(cost)-1, dict())
