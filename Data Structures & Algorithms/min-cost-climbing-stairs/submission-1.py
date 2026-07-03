class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(len(cost) - 1, -1, -1):

            # if we're at he last index or the 2nd last index
            if i + 2 > (len(cost) - 1):
                continue

            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])