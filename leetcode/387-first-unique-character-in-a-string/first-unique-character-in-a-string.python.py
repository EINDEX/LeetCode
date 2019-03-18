class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket = {chr(k):0 for k in range(97,123)}
        for i, k in enumerate(s):
            if bucket[k] == 0:
                bucket[k] = i+1
            elif bucket[k] > 0:
                bucket[k] = -1
       
        for i, k in enumerate(s):
            if bucket[k] > 0:
                return i
        else:
            return -1

