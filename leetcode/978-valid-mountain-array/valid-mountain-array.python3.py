class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) == 0 or len(A) == 1:
            return False
        now = A[0] - 1
        if A[0] >= A[1]:
            return False
        if A[-2] <= A[-1]:
            return False
        flag = True
        for i in A:
            if i > now and flag:
                now = i
            elif i < now and flag:
                flag = False
                now = i
            elif i < now and not flag:
                now = i
            else:
                return False
        return True