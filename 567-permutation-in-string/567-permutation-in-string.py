class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # initial window
        s1d = dict()
        s2d = dict()
        for i in range(len(s1)):
            s1d[s1[i]] = s1d.get(s1[i], 0)+1
            s2d[s2[i]] = s2d.get(s2[i], 0)+1
        # move window
        l, r = 0, i
        while True:
            if s1d == s2d:
                return True
            # remove left element
            s2d[s2[l]] -= 1
            if s2d[s2[l]] == 0:
                del(s2d[s2[l]])
            l += 1
            r += 1
            if r >= len(s2):
                break
            # insert right element
            s2d[s2[r]] = s2d.get(s2[r], 0)+1
        
        return False
