class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        L = matrix[0]
        for line in matrix[1:]:
            for x in range(len(line)-1):
                if line[x+1] != L[x]:
                    return False
            L = line
        return True
