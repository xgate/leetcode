class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j] += self.mv(i, j-1)+self.mv(i-1, j)-self.mv(i-1, j-1)
    
    # matrix value
    def mv(self, row, col):
        if row < 0 or col < 0: 
            return 0
        return self.matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2][col2]-self.mv(row2, col1-1)-self.mv(row1-1, col2)+self.mv(row1-1, col1-1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
