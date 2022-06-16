class Solution:
    
    def palindromeRange(self, s, l, r):
        while s[l] == s[r]:
            if l >= 1 and r < len(s)-1:
                l -= 1
                r += 1
            else:
                break
        if s[l] != s[r]:
            l += 1
            r -= 1
        return (l, r)
    
    def longestPalindrome(self, s: str) -> str:
        d = dict()
        maxLen = 0
        for i in range(len(s)):
            l1, r1 = self.palindromeRange(s, i, i)
            length1 = r1-l1+1
            # consider 'bb', 'aaaa'
            l2 = r2 = length2 = 0
            if i < len(s)-1 and s[i] == s[i+1]:
                l2, r2 = self.palindromeRange(s, i, i+1)
                length2 = r2-l2+1            
            if length1 >= length2:
                l, r = l1, r1
            else:
                l, r = l2, r2            
            
            length = r-l+1
            if length > 1:
                d[length] = (l, r)
            maxLen = max(length, maxLen)
        
        if maxLen == 1:
            return s[0]
        
        ans = ""
        l, r = d[maxLen]
        for i in range(l, r+1):
            ans += s[i]    
        return ans
