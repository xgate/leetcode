class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = list()
        sp = "".join(sorted(p))
        for i in range(len(s)-len(p)+1):
            subs = s[i:i+len(p)]
            if "".join(sorted(subs)) == sp:
                ans.append(i)
        return ans