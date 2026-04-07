import operator as op;

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for t in tokens:
            if t in ops.keys():
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(ops[t](b, a))
            else:
                stack.append(t)
        return int(stack[0])
