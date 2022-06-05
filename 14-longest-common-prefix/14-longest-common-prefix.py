class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        minLen = min(len(s) for s in strs)    
        commonPrefix = list()
        for i in range(minLen):
            if all(strs[j][i] == strs[0][i] for j in range(len(strs))):
                commonPrefix.append(strs[0][i])
            else:
                break
        return "".join(commonPrefix)
    