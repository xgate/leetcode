class Solution:
    def matched(self, pattern, word):
        replace = dict()
        used = dict()
        for i in range(len(word)):
            p = replace.get(word[i])
            if not p:
                if used.get(pattern[i]): return False
                replace[word[i]] = pattern[i]
                used[pattern[i]] = True
            else:
                if p != pattern[i]:
                    return False                
        return True
            
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:        
        ans = list()
        for i in range(len(words)):
            if self.matched(pattern, words[i]):
                ans.append(words[i])
        return ans
    