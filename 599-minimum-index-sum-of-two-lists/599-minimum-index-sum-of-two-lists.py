class Solution:
    
    def r2dict(self, rs):
        d = dict()
        for i in range(len(rs)):
            d[rs[i]] = i
        return d
    
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        r1 = self.r2dict(list1)
        r2 = self.r2dict(list2)
        commons = list(set(r1.keys()) & set(r2.keys()))
        mergedR = {r: r1[r]+r2[r] for r in commons}
        sortedR = sorted(mergedR.items(), key = lambda item: item[1])
        return list(map(lambda x: x[0], filter(lambda x: x[1] == sortedR[0][1], sortedR)))
