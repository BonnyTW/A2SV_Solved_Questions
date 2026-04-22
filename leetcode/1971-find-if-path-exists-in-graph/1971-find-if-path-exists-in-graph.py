from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)

        for i in range(len(edges)):
            row = edges[i]
            graph[row[0]].append(row[1]) 
            graph[row[1]].append(row[0])

        def DFS(source,destination,visited):
            if source == destination:
                return True
            visited.add(source)

            for neighbour in graph[source]:
                if neighbour not in visited:
                    if DFS(neighbour,destination,visited):
                        return True
            return False
        my_set = set()

        return DFS(source,destination,my_set)
        
    
        

        




        