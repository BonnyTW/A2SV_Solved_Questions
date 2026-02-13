class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for i in range(4):
            res=[]
            for i in range(len(mat[0])):
                temp=[]
                for j in range(len(mat)-1,-1,-1):
                    temp.append(mat[j][i])
                res.append(temp)
            mat[:]=res
            if mat==target:
                return True
        return False

        
