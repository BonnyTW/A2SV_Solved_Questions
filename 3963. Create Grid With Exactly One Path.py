class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        
        for i in range(m):
            if i == 0:
                ans.append('.'*n)
            else:
                temp = '#' * (n-1)
                temp += '.'
                ans.append(temp)
        return ans
                

        
        
        
