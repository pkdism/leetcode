"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
"""


class Trie:
    def __init__(self):
        self.trie = {"" : set()}
        self.words = set()

    def insert(self, word):
        for k in range(len(word)+1):
            if word[:k] in self.trie:
                continue
            self.trie[word[:k-1]].add(word[:k])
            self.trie[word[:k]] = set()
        self.words.add(word)
        
    def search(self, word: str):
        return word in self.words
        
    def startswith(self, prefix: str):
        return prefix in self.trie


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        res = []
        
        w = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def check(i, j, index, visited):
            if trie.search(index):
                res.append(index)
            if trie.startswith(index):
                for t in w:
                    i_dash, j_dash = i + t[0], j + t[1]
                    if i_dash >= 0 and i_dash < m and j_dash >= 0 and j_dash < n and not (i_dash, j_dash) in visited:
                        check(i_dash, j_dash, index + board[i_dash][j_dash], visited.union({(i_dash, j_dash)}))
                
                
        for i in range(m):
            for j in range(n):  
                check(i, j, board[i][j], {(i, j)})
        
        return list(set(res))