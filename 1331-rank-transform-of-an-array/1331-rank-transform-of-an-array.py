class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sa = sorted(list(set(arr)))
        indexes = {sa[i]: i+1 for i in range(len(sa))}
        return [indexes[arr[i]] for i in range(len(arr))]
