class Solution:
    def isHappy(self, n: int) -> bool:
        d = {n: 1}
        while True:
            n = sum([int(c) ** 2 for c in str(n)])
            if n == 1:
                return True
            if n in d:
                break
            d[n] = 1
        
        return False
    