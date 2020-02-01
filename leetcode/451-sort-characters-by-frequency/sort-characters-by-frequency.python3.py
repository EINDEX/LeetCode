class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}
        for i in s:
            m.setdefault(i, 0)
            m[i] += 1
        return ''.join([k*v for k,v in sorted(m.items(), key=lambda x:x[1], reverse=True)])
                
            
        