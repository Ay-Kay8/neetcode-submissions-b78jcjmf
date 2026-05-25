class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], [] # stack will contain our parenthesis

        def backtrack(nb_open, nb_closed):
            if nb_open == nb_closed == n:
                res.append("".join(stack))
                return
            
            # Only add open parenthesis if open < n
            if nb_open < n:
                stack.append("(")
                backtrack(nb_open + 1, nb_closed)
                stack.pop()

            # Only add a closing parenthesis if closed < open
            if nb_closed < nb_open and nb_closed < n:
                stack.append(")")
                backtrack(nb_open, nb_closed + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res            