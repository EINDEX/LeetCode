class Solution:
    def tribonacci(self, n: int) -> int:
        x = [0, 1, 1]
        if n < len(x):
            return x[n]
        for _ in range(n-2):
            x[0], x[1], x[2] = x[1], x[2], sum(x)
        return x[2]