class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
    
        def backtrack(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    # Inclusive/Exclusive, we want to include j so we do j + 1
                    partition.append(s[i:j+1])
                    backtrack(j + 1) # backtrack on the rest
                    partition.pop()

        backtrack(0)
        return res

    # i: left bound, j: right bound    
    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        