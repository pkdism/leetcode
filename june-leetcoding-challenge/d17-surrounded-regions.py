"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""


class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        
        def is_valid(i, j, rows, cols):
            return i >= 0 and i < rows and j >= 0 and j < cols
        
        def dfs(board, i, j, rows, cols):
            
            di = [-1, 0, 1, 0]
            dj = [0, 1, 0, -1]
            
            if(board[i][j] == 'O'):
                board[i][j] = 'E'
                for l in range(4):
                    row = i + di[l]
                    col = j + dj[l]
                    if(is_valid(row, col, rows, cols) and board[row][col] == 'O'):
                        dfs(board, row, col, rows, cols)
                        
        rows = len(board)
        
        if(rows < 2):
            return

        cols = len(board[0])

        for i in range(rows):
            if(board[i][0] == 'O'):
                dfs(board, i, 0, rows, cols)
            if(board[i][cols-1] == 'O'):
                dfs(board, i, cols-1, rows, cols)

        for i in range(cols):
            if(board[0][i] == 'O'):
                dfs(board, 0, i, rows, cols)
            if(board[rows-1][i] == 'O'):
                dfs(board, rows-1, i, rows, cols)
                
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif(board[i][j] == 'E'):
                    board[i][j] = 'O'