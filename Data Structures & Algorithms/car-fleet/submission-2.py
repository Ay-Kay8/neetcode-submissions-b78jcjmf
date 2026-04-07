class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {} # (pos, speed)
        fleet = 1
        for i in range(len(position)):
            d[position[i]] = speed[i]
        d = dict(sorted(d.items(), reverse=True))

        stack = []
        for pos, speed in d.items():
            timeToTarget = (target - pos) / speed
            if not stack:
                stack.append(timeToTarget)
            elif stack[-1] < timeToTarget:
                stack.append(timeToTarget)
        return len(stack)