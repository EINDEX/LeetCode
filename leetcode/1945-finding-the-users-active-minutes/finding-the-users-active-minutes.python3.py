class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        data = {}
        res = [0]*k
        for log in logs:
            data.setdefault(log[0],set())
            data[log[0]].add(log[1])
        for k, v in data.items():
            res[len(v)-1] += 1
        return res