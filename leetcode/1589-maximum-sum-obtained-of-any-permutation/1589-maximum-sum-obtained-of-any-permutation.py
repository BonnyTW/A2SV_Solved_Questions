class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
        # [1,1,-1,0,-1,0]->[1,2,1,1,0,0] -> max_freq = max(nums) -->[4,5,3,2,1] --------[2,1,1,1,0]*[5,4,3,2,1]->[10,4,3,2,0]=19

        psum=[0]*(len(nums)+1)

        for s,e in requests:
            psum[s] +=1
            psum[e+1]-=1

        for i in range(1,len(psum)):
            psum[i] += psum[i-1]

        print(psum)
        nums.sort(reverse=True)
        psum.sort(reverse=True)
        print(psum)
        
        for i in range(len(nums)):
            psum[i]*=nums[i]

        return sum(psum)% (10**9 + 7)

        

        
