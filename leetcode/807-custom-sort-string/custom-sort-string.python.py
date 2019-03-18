class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        data = [0 for _ in range(len(S))]
        for i,k in enumerate(list(S)):
            data[i]=T.count(k)
            T = T.replace(k, '')
        return ''.join([S[i]*k for i, k in enumerate(data)]) + T
