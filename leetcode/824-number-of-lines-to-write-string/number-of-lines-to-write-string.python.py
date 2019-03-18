class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_space = 0
        line = 0
        for i in range(len(S)):
            width = widths[ord(S[i]) - ord('a')]
            if line_space + width <= 100:
                line_space += width
            else:
                line += 1
                line_space = width
        return [line+1, line_space]
        
        
