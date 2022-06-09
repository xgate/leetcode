from bisect import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = list()
        for i in range(len(numbers)):
            a = numbers[i]
            b = target-numbers[i]
            j = bisect(numbers, b, i+1)
            if numbers[j-1] == b and a+b == target:
                ans.extend([i+1, j])
                break
        return ans
