class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
#         d = {}
#         for a, b in pairs:
#             if a in d: 
#                 if b < d[a]:
#                     d[a] = b
#             else:
#                 d[a] = b
            
#         r =[(a,b) for a,b in d.items()]
        pairs.sort(key=lambda a:a[1])
        # print(r)
        l = 1
        t = pairs[0][1]
        for x in pairs:
            if x[0] > t:
                t = x[1]
                l += 1
        return l
                