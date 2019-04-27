class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last, now = 0, 0
        for i in range(2, len(cost) + 1):
            last, now = now, min(now + cost[i-1], last + cost[i-2])
        return now