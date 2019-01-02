class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # 将字符串单数位和偶数位分别排序组成一个新串检测是否出现过
        r =  set()
        for w in A:
            c = "".join(sorted([w[x] for x in range(len(w)) if x % 2]) + sorted([w[x] for x in range(len(w)) if x % 2 == 0]))
            if c not in r:
                r.add(c)
        return len(r)