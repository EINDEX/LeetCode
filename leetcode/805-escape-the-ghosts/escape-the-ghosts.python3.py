class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        l = abs(target[0]) + abs(target[1])
        for x in ghosts:
            if abs(x[0]-target[0]) + abs(x[1]-target[1]) <= l:
                return False
        return True