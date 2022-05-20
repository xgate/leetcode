class Solution:
    def nextRow(self, up: List[int]) -> List[int]:
        row = [1]
        for i in range(1, len(up)):
            n = up[i-1]+up[i]
            row.append(n)
        row.append(1)
        return row
    
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        result = [1,1]
        for i in range(1, rowIndex):
            result = self.nextRow(result)
        return result
