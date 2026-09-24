class PrefixTree:

    def __init__(self):
        self.head = {} # letter: {}

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c in curr:
                curr = curr[c]
                continue
            curr[c] = {}
            curr = curr[c]
        curr["$"] = {} # This is an end of word

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c in curr:
                curr = curr[c]
                continue
            
            return False
        return "$" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c in curr:
                curr = curr[c]
                continue
            
            return False
        return True