class Solution:
    def getLucky(self, s: str, k: int) -> int:
        f = ''.join([str(ord(x)-ord('a')+1) for x in s])

        for _ in range(k):
            f = sum([int(i) for i in str(f)])

        return f