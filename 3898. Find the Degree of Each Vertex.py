class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for v in matrix:
            ans.append(sum(v))
        
        return ans
        
