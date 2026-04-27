class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        street_directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        
        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols 
        
        def DFS(row,col):

            if (row,col) == (rows - 1, cols - 1):
                return True
            
            visited[row][col] = True
            
            for dr,dc in street_directions[grid[row][col]]:
                new_r = row + dr
                new_c = col + dc

                if inbound(new_r,new_c) and not visited[new_r][new_c]:
                    if opposite[(dr,dc)] in street_directions[grid[new_r][new_c]]:
                        if DFS(new_r,new_c):
                            return True
            return False


        return DFS(0,0)