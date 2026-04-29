class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]

        def DFS(source):
            if source == len(graph) - 1:
                res.append(path[:])
                return 
            for nei in graph[source]:
                path.append(nei)
                DFS(nei)
                path.pop()
        DFS(0)
        return res