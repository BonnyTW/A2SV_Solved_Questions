class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mi_s=[]
        res=0

        heights=[float('-inf')] + heights + [float('-inf')]
        
        for i in range(len(heights)):
            while mi_s and heights[mi_s[-1]] > heights[i]:
                idx=mi_s.pop()
                width=i-mi_s[-1]-1
                
                res=max(res,heights[idx]*width)

            mi_s.append(i)
        return res