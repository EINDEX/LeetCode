class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        in_map = {}
        exit_map = {}
        start = 10**5
        end = 0
        for segment in segments:
            in_map.setdefault(segment[0],set())
            in_map[segment[0]].add(segment[2])
            if segment[0] < start:
                start = segment[0]
            exit_map.setdefault(segment[1],set())
            exit_map[segment[1]].add(segment[2])
            if segment[1] > end:
                end = segment[1]

        now_color = set()
        point = start
        result = []
        
        for point in sorted(list(set(in_map.keys()) | set(exit_map.keys()))):
            # print(point, result)
            if now_color:
                result[-1][1] = point
            if point in exit_map and point in in_map:
                now_color -= exit_map[point]
                now_color |= in_map[point]
            elif point in exit_map:
                now_color -= exit_map[point]
            elif point in in_map:
                now_color |= in_map[point]
            if now_color:
                    result.append([point, point, sum(now_color)])
        return result
                
        