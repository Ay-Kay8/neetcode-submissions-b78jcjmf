class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        word = ""

        # i: index of the current digit
        def dfs(i):
            nonlocal word

            if i == len(digits):
                if word != "":
                    res.append(word)
                return

            for letter in dict[digits[i]]:
                word += letter
                dfs(i + 1)
                word = word[:-1]
        
        dfs(0)
        return res

            