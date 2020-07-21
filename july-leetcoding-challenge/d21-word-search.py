"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board, word):
        def util(index, i, j):
        
            if self.found: 
                return

            if index == k:
                self.found = True 
                return 

            if i < 0 or i >= m or j < 0 or j >= n: return 
            curr = board[i][j]
            if curr != word[index]: 
                return

            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                util(index + 1, i+x, j+y)
            board[i][j] = curr
        
        self.found = False
        m, n, k = len(board), len(board[0]), len(word)
        
        for i, j in product(range(m), range(n)):
            if self.found: return True
            util(0, i, j)
        return self.found