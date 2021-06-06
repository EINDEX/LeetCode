class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        data = {}
        for x in nums:
            data.setdefault(x, 0)
            data[x] += 1
        keys = sorted(list(data.keys()), reverse=True)
        m = 0
        s = 0
        for key in keys[:-1]:
            s += data[key]
            m += s

        return m
