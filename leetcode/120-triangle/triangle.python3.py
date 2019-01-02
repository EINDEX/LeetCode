class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for l in range(len(triangle)-1-1, -1, -1):
            for x in range(len(triangle[l])):
                triangle[l][x] += min(triangle[l+1][x], triangle[l+1][x+1])
        return triangle[0][0]