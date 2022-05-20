class Solution:
    def valid(self, board: List[List[str]], row, col) -> bool:
        d = dict()
        for i in range(3):
            for j in range(3):
                s = board[row+i][col+j]
                if s.isdigit():
                    if s in d:
                        return False
                    d[s] = 1
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            d = dict()
            for j in range(9):
                s = board[i][j]
                if s.isdigit():
                    if s in d:
                        return False
                    d[s] = 1
        
        # col
        for i in range(9):
            d = dict()
            for j in range(9):
                s = board[j][i]
                if s.isdigit():
                    if s in d:
                        return False
                    d[s] = 1
        
        # sub-boxes
        for i in range(3):
            for j in range(3):
                if not self.valid(board, i*3, j*3):
                    return False
        
        return True
