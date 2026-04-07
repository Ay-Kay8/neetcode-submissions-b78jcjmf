import operator as op;

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": lambda a, b: int(a / b), # avoid 6 / -132 = -1
        }
        # ops["+"](3, 4)

        t = list(reversed(tokens))
        stack = []
        while len(t) != 0:
            # print(t)
            # print(stack)
            if t[-1] in ops.keys():
                res = ops[t[-1]](int(stack[-2]), int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(res)
                t.pop()
            else:
                stack.append(t.pop())
        return int(stack[0])