class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxvolume=0
        while left<right:
            w=right-left
            h=min(height[left],height[right])
            maxvolume=max(maxvolume,h*w)
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
                
        return maxvolume

         
