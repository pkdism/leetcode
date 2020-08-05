"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
"""


class Trienode:
    def __init__(self):
        self.children = {}
        self.end = 0
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for letter in word:
            node = node.children.setdefault(letter, Trienode())
        node.end = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def util(node, index):
            n = len(word)
            if index == n:
                return node.end
            if word[index] == ".":
                for child in node.children:
                    if util(node.children[child], index+1):
                        return True
            if word[index] in node.children:
                return util(node.children[word[index]], index + 1)
            
            return False
        return util(self.root, 0)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)