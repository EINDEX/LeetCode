class Solution:
    def searchMatrix(self, m, target):
        """
        :type m: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not m:
            return False
        w = len(m[0])
        h = len(m)
        x = w - 1
        while x >= 0:
            if m[0][x] < target:
                for y in range(1, h):
                    if m[y][x] == target:
                        return True
            elif m[0][x] == target:
                return True
            x -= 1
        return False
            