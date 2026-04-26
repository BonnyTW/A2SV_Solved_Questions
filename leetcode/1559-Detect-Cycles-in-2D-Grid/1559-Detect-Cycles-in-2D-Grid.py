from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def DFS(r, c, pr, pc):
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc):
                    continue

                if grid[nr][nc] != grid[r][c]:
                    continue

                # if not visited → go deeper
                if not visited[nr][nc]:
                    if DFS(nr, nc, r, c):
                        return True

                # if visited AND not parent → cycle
                elif (nr, nc) != (pr, pc):
                    return True

            return False

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if DFS(r, c, -1, -1):
                        return True

        return False