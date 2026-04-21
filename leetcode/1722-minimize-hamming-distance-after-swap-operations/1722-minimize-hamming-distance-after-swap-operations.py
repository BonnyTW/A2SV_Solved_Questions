

from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        
        # Step 1: Build graph
        graph = defaultdict(list)
        for u, v in allowedSwaps:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        result = 0
        
        # Step 2: BFS for connected components
        for i in range(n):
            if visited[i]:
                continue
            
            queue = deque([i])
            visited[i] = True
            component = []
            
            while queue:
                node = queue.popleft()
                component.append(node)
                
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
            
            # Step 3: Count frequencies
            count = defaultdict(int)
            for idx in component:
                count[source[idx]] += 1
            
            # Step 4: Match with target
            for idx in component:
                if count[target[idx]] > 0:
                    count[target[idx]] -= 1
                else:
                    result += 1
        
        return result