class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(n):
            if n==0:
                return [1]
            prev=helper(n-1)
            cur=[1]
            for i in range(1,len(prev)):
                cur.append(prev[i-1]+prev[i])
            cur.append(1)
            return cur
        return helper(rowIndex)





        
        
        
        
        
        