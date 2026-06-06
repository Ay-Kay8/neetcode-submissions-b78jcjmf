class Node:
    def __init__(self):
        # { 'a' : Node }
        self.children = {}
        self.is_end_of_world = False

class PrefixTree:

    def __init__(self):
        self.root = Node()        

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.is_end_of_world = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
            
        return curr.is_end_of_world

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return True
