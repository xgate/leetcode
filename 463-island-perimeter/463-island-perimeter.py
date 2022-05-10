class Solution:
    def isWater(self, grid, row, col, i, j):
        if i >= row or i < 0:
            return True
        if j >= col or j < 0:
            return True
        if grid[i][j] == 0:
            return True
        
        return False
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        row = len(grid)
        for i in range(0, row):
            col = len(grid[i])
            for j in range(0, col):
                if grid[i][j] == 1:
                    if self.isWater(grid, row, col, i-1, j):
                        p += 1
                    if self.isWater(grid, row, col, i, j+1):
                        p += 1
                    if self.isWater(grid, row, col, i+1, j):
                        p += 1
                    if self.isWater(grid, row, col, i, j-1):
                        p += 1
        
        return p
