class Solution:
    def analysis(self, word):
        d = dict()
        for i in range(len(word)):
            d[word[i]] = d.get(word[i],0)+1
        return d
    
    def includes(self, d1, d2):
        for k in d2.keys():
            f = d1.get(k)
            if not f: return False
            if f < d2[k]: return False
        return True
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq1 = dict()
        for i in range(len(words1)):
            freq1[i] = self.analysis(words1[i])
            
        freq2 = dict()
        for i in range(len(words2)):
            freq2[i] = self.analysis(words2[i])
        
        merged = dict()
        for i in range(len(words2)):
            for k in freq2[i].keys():
                merged[k] = max(merged.get(k, 0), freq2[i][k])
        
        ans = list()
        for i in range(len(words1)):
            if self.includes(freq1[i], merged):
                ans.append(words1[i])
                
        return ans
