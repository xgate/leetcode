class Solution:
    
    def climb(self, n, mem):
        mem[n] = mem.get(n) if n in mem else self.climb(n-1, mem)+self.climb(n-2, mem)
        return mem[n]
    
    def climbStairs(self, n: int) -> int:
        return self.climb(n, {1: 1, 2: 2})
