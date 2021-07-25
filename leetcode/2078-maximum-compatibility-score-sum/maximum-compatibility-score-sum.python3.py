class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        cal = []
        for x in range(len(mentors)):
            cal.append([0] * len(students))
            
        for x in range(len(students)):
            for y in range(len(mentors)):
                cal[x][y] = sum([int(students[x][i] == mentors[y][i]) for i in range(len(students[0]))])
                print(x, y,cal[x][y])
        
        max_result = [0]
        def deepin(used=set(), row=0, res=0):
            if row == len(mentors):
                if res > max_result[0]:
                    max_result[0]=res
                return res
            
            for i, x in enumerate(cal[row]):
                if i in used:
                    continue
                deepin(used | set([i]), row + 1, res+x)
            
        deepin(set())
        return max_result[0]
                