# refactoring 
class Solution:
    
    def palindromeLen(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1
    
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            len1 = self.palindromeLen(s, i, i)
            # consider 'bb', 'aaaa'
            len2 = self.palindromeLen(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i-int((length-1)/2)
                end = i+int(length/2)
        
        return s[start:end+1]
