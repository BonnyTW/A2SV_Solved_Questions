class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)-1,-1,-1):
                temp.append(matrix[j][i])
            res.append(temp)
        matrix[:]=res


        
