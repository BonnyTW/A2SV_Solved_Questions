class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ps=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    self.ps[i+1][j+1] = matrix[i][j]
                elif i == 0 :
                    self.ps[i+1][j+1] = self.ps[i+1][j] + matrix[i][j]
                elif j == 0:
                    self.ps[i+1][j+1] = self.ps[i][j+1] + matrix[i][j]
                else:self.ps[i+1][j+1] = (self.ps[i][j+1]+ self.ps[i+1][j]- self.ps[i][j]+ matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.ps[row2+1][col2+1]- self.ps[row1][col2+1]- self.ps[row2+1][col1] + self.ps[row1][col1])