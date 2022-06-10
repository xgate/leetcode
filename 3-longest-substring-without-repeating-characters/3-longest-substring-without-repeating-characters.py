class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ss = set()
        l = r = ans = 0
        while r < len(s):
            if s[r] in ss:
                while s[l] != s[r]:
                    ss.remove(s[l])
                    l += 1
                l += 1          
            ss.add(s[r])
            ans = max(ans, r-l+1)
            r += 1
        return ans
