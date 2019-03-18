class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        s.sort()
        g.sort()
        for x in g:
            while s:
                t = s.pop(0)
                if x <= t:
                    count += 1
                    break
        return count


