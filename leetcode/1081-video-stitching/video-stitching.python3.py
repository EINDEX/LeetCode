class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # r = [false for _ in range(T+1)]
        t = 0
        res = 0
        
        flag = True
        while flag:
            it = t
            flag = False
            for i in clips:
                if i[0] <= t and i[1] > it:
                    it = i[1]
                    flag = True
            if flag:
                t = it
                res += 1
            if t >= T:
                break
        
        return res if t >= T else -1
                      
        