class Solution:
    
    def back(self, cds, start, acc, ans, target):
        if sum(acc) > target:
            return
        if sum(acc) == target:
            ans.append(acc.copy())
            return
        for i in range(start, len(cds)):
            acc.append(cds[i])
            self.back(cds, i, acc, ans, target)
            acc.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        self.back(sorted(candidates), 0, list(), ans, target)
        return ans
    