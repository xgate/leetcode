class Solution:        
    def sim(self, s: str) -> str:
        ns = ""
        bc = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '#':
                bc += 1
            else:
                if bc <= 0:
                    ns += s[i]
                if bc > 0: 
                    bc -= 1
        
        return ns

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.sim(s) == self.sim(t)
