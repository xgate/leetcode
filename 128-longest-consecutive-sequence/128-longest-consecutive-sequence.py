class Solution:
    
    def union(self, nums, indexes, parents, n):
        if parents.get(n):
            return parents[n]
        index = indexes.get(n)
        if index is None:
            return n+1
        else:
            parents[n] = self.union(nums, indexes, parents, nums[index]-1)
            return parents[n]
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        indexes = dict()
        for i in range(len(nums)):
            indexes[nums[i]] = i        
        
        parents = dict()
        for i in range(len(nums)):
            if parents.get(nums[i]) is None:
                parents[nums[i]] = self.union(nums, indexes, parents, nums[i])
        
        counts = dict()
        maxCount = 0
        for p in list(parents.values()):
            counts[p] = counts.get(p, 0)+1
            maxCount = max(maxCount, counts[p])
        
        return maxCount
    