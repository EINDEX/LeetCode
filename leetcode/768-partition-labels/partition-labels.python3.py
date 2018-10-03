class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = {k:i for i,k in enumerate(list(S))}
        res = []
        lattes = set()
        index = 0
        for i, x in enumerate(list(S)):
            if x not in lattes:
                if all(i > d[k] for k in list(lattes)) and i != 0:
                    lattes = set()
                    res.append(i - sum(res))
                    
                lattes.add(x)
        if res:
            res.append(len(S)-sum(res))
        else:
            res.append(len(S))
        return res