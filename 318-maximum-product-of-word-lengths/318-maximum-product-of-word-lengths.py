class Solution:
    def distinct(self, w1, w2) -> bool:
        d = dict()
        for c in w1:
            d[c] = 1
        for c in w2:
            if c in d:
                return False
        return True
    
    def maxProduct(self, words: List[str]) -> int:
        mx = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.distinct(words[i], words[j]):
                    m = len(words[i]) * len(words[j])
                    mx = max(m, mx)
        return mx