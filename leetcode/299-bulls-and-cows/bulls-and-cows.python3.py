class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        sa = []
        sb = []
        for a, b in zip(secret, guess):
            if a == b:
                A += 1
            if a != b:
                sa.append(a)
                sb.append(b)
        sa.sort()
        sb.sort()
        B = 0
        i, j  = 0, 0
        while i < len(sa) and j < len(sb):
            if sa[i] == sb[j]:
                B+=1
                i+=1
                j+=1
            elif  sa[i] < sb[j]:
                i +=1
            else:
                j +=1
        return f"{A}A{B}B"