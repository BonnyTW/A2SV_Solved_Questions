class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < columns

        
        def DFS(grid,visited,row,col):
            visited[row][col] = True
            perimeter = 0

            for r,c in directions:
                new_row = row + r
                new_col = col + c

                if not inbound(new_row,new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                elif inbound(new_row,new_col) and not visited[new_row][new_col]:
                    DFS(grid,visited,new_row,new_col)

            return perimeter

        

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    return DFS(grid,visited,row,col)
        return False