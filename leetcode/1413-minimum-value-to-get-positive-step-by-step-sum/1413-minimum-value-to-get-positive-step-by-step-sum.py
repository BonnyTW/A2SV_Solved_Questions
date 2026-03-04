class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # [-3,2,-3,4,2] --> [-3,-1,-4,0,2]
        # [1,2]->[1,3]


        psum=0
        min_num=float('inf')
        for num in nums:
            psum+=num
            min_num=min(min_num,psum)


    
        if min_num>0:
            return 1
        else:
            return abs(min_num)+1

        

        