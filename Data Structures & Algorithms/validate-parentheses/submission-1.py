class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case "(":
                    stack.append("(")
                case "{":
                    stack.append("{")
                case "[":
                    stack.append("[")
                case ")":
                    if len(stack) == 0 or stack[-1] != "(":
                        return False
                    stack.pop()
                case "}":
                    if len(stack) == 0 or stack[-1] != "{":
                        return False
                    stack.pop()
                case "]":
                    if len(stack) == 0 or stack[-1] != "[":
                        return False
                    stack.pop()
                
        return len(stack) == 0
        