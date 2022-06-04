class Solution:
    
    def markLeftDown(self, board, incr, row, col, n):
        if row >= n or col < 0:
            return
        board[row][col] += incr
        return self.markLeftDown(board, incr, row+1, col-1, n)
    
    def markDown(self, board, incr, row, col, n):
        if row >= n:
            return
        board[row][col] += incr
        return self.markDown(board, incr, row+1, col, n)
    
    def markRightDown(self, board, incr, row, col, n):
        if row >= n or col >= n:
            return
        board[row][col] += incr
        return self.markRightDown(board, incr, row+1, col+1, n)
    
    def mark(self, board, incr, row, col, n):
        self.markLeftDown(board, incr, row+1, col-1, n)
        self.markDown(board, incr, row+1, col, n)
        self.markRightDown(board, incr, row+1, col+1, n)
            
    def transform(self, board, n, Q):
        newBoard = list()
        for i in range(n):
            eachRow = list()
            for j in range(n):
                if board[i][j] == Q:
                    eachRow.append('Q')
                else:
                    eachRow.append('.')
            newBoard.append("".join(eachRow))
        return newBoard
        
    def place(self, board, row, n, ans):
        Q = 128        
        if row == n:
            ans.append(self.transform(board, n, Q))
            return        
        for i in range(n):
            if board[row][i] == 0:
                board[row][i] = Q
                self.mark(board, 1, row, i, n)
                self.place(board, row+1, n, ans)
                self.mark(board, -1, row, i, n)
                board[row][i] = 0
   
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = list()
        board = [[0 for i in range(n)] for j in range(n)]
        self.place(board, 0, n, ans)
        return ans
