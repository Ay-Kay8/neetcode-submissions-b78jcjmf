class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (value, index)
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                _, index = stack.pop()
                res[index] = (i - index)
            stack.append((n, i))
        return res

        