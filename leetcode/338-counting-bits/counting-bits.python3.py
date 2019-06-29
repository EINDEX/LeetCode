class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(x).count('1') for x in range(num+1)]
            