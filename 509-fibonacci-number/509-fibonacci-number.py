class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(1, n):
            t = b
            b = a+b
            a = t
        return b
