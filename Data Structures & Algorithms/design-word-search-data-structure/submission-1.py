class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:

            if letter not in curr.children:
                curr.children[letter] = TrieNode()
                
            curr = curr.children[letter]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):

            if i == len(word): 
                return node.is_end_of_word
            
            if word[i] == '.':
                # Skip the current Trie Node and run search recursively on all others
                for child in node.children.values():
                    # Mistake here, on the first call of this, we exit right after
                    # the first call because of the return
                    # So we would only be checking the first value
                    # return dfs(i + 1, child)

                    # We have to do something like this
                    if dfs(i + 1, child):
                        return True
            
            if word[i] not in node.children:
                return False
            
            return dfs(i + 1, node.children[word[i]])
        return dfs(0, self.root)