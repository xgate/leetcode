from queue import Queue

class Solution:
    def isLand(self, grid, row, col, i, j):
        if i >= row or i < 0:
            return False
        if j >= col or j < 0:
            return False
        return grid[i][j] == 1
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = Queue()
        result = 0
        row = len(grid)
        col = len(grid[0])
        pos = [(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:                    
                    grid[i][j] = 0
                    q.put((i,j))
                    area = 0
                    while not q.empty():
                        y, x = q.get()
                        area += 1                        
                        for ii, jj in pos:
                            if self.isLand(grid, row, col, y+ii, x+jj):
                                q.put((y+ii, x+jj))
                                grid[y+ii][x+jj] = 0
                        
                    result = max(area, result)

        return result
