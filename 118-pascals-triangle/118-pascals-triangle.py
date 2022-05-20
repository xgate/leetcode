class Solution:
    def nextRow(self, up: List[int]) -> List[int]:
        row = [1]
        for i in range(1, len(up)):
            n = up[i-1]+up[i]
            row.append(n)
        row.append(1)
        return row
            
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        result.extend(self.nextRow(result[i-1]) for i in range(2, numRows))
        return result
