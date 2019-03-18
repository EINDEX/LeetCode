class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for x in A:
            if x in s:
                return x
            else:
                s.add(x)
