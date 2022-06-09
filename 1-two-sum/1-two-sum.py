from bisect import bisect

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = list()
        snums = sorted(nums)
        for i in range(len(snums)):
            a = snums[i]
            b = target-snums[i]
            j = bisect(snums, b, i+1)
            if snums[j-1] == b:
                ai = nums.index(a)
                bi = nums.index(b)
                if ai == bi:
                    bi = nums.index(b, bi+1)
                ans.extend([ai, bi])
                break
        return ans
