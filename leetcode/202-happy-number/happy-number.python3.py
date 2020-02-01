class Solution:
    def isHappy(self, n: int) -> bool:
        path = set()
        while n != 1:
            if n in path:
                return False
            path.add(n)
            res = 0
            while n:
                res += (n % 10)**2
                n = n // 10
            n = res
        return True
        