class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        layers = []

        num_layers = min(m, n) // 2

        for layer in range(num_layers):

            vals = []

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            # top row
            for c in range(left, right + 1):
                vals.append(grid[top][c])

            # right column
            for r in range(top + 1, bottom):
                vals.append(grid[r][right])

            # bottom row
            for c in range(right, left - 1, -1):
                vals.append(grid[bottom][c])

            # left column
            for r in range(bottom - 1, top, -1):
                vals.append(grid[r][left])

            layers.append(vals)

        ans = [row[:] for row in grid]

        for i in range(len(layers)):
            kk = k % len(layers[i])
            layers[i] = layers[i][kk:] + layers[i][:kk]

        for layer in range(num_layers):

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            idx = 0

            # top row
            for c in range(left, right + 1):
                ans[top][c] = layers[layer][idx]
                idx += 1

            # right column
            for r in range(top + 1, bottom):
                ans[r][right] = layers[layer][idx]
                idx += 1

            # bottom row
            for c in range(right, left - 1, -1):
                ans[bottom][c] = layers[layer][idx]
                idx += 1

            # left column
            for r in range(bottom - 1, top, -1):
                ans[r][left] = layers[layer][idx]
                idx += 1

        return ans
