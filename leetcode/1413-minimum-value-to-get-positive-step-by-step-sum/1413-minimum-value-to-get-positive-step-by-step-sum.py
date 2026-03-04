class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # [-3,2,-3,4,2] --> [-3,-1,-4,0,2]
        # [1,2]->[1,3]

        psum=[nums[0]]

        for num in nums[1:]:
            psum.append(psum[-1]+num)
        print(psum)
        
        min_num=min(psum)
        if min_num>0:
            return 1
        else:
            return abs(min_num)+1

        

        