class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for c in s:
            if c in openToClosed:
                stack.append(c)
            elif len(stack) != 0 and openToClosed[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return len(stack) == 0