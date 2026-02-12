class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seen=set()
        for i in range(len(matrix)):
            if 0 in set(matrix[i]):
                seen.add(i)


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(len(matrix)):
                        matrix[k][j]=0
                        if j==k:
                            continue
                    
        for i in seen:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
                    
                
                    
        
                
        
        

        
