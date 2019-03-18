class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for x in range(left, right+1):
            if all([i!='0' and x%int(i)==0 for i in list(str(x))]):
                res.append(x)
        return res
