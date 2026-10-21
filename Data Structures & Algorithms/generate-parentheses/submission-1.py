class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = ""
        res = []

        def dfs(opened, closed):
            nonlocal path

            if len(path) == 2*n:
                res.append(path)
                return 

            # only add opened parenthesis if:
            if opened < n:
                path += "("
                dfs(opened + 1, closed)
                path = path[:-1]


            # only add closing parenthesis if:
            if closed < opened:                
                path += ")"
                dfs(opened, closed + 1)
                path = path[:-1]
            
            # path = path[:-1]

        dfs(0, 0)

        return res