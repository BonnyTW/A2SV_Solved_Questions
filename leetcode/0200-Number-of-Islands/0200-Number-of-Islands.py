class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions =[(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols



        def DFS(grid,row,col):
            if grid[row][col] == '0' or row >= rows or 0 > row or col >= cols or 0 > col:
                return 
            
            grid[row][col] = '0'

            for row_change,col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
            
                if inbound(new_row,new_col) and grid[new_row][new_col] == '1':
                    DFS(grid,new_row,new_col)
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count +=1 
                    DFS(grid,row,col)
        return count