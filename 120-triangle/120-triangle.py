class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j-1 < 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j >= len(triangle[i-1]):
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        
        lastRow = len(triangle)-1
        x = triangle[lastRow][0]
        for i in range(len(triangle[lastRow])):
            x = min(x, triangle[lastRow][i])
        return x
