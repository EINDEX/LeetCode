class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        m = 0
        while i < j:
            h = min(height[i], height[j])
            s = h * (j - i)
            if s > m:
                m = s
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return m
        