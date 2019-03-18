class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(graph)
        
        def inner(node):
            if node == N-1: 
                return [[N-1]]
            
            ans = []
            for nei in graph[node]:
                for path in inner(nei):
                    ans.append([node]+path)
            return ans
        
        return inner(0)
        
