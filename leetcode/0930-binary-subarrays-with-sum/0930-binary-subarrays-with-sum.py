class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # [1,0,1,0,1] -- > [0,1,1,2,2,3]
        # {0:1,1:2,2:2,3:1} 1+1+2=4

        my_dict=Counter({0:1})
        
        psum=0
        count=0
        for num in nums:
            psum+=num

            if psum - goal in my_dict:
                count += my_dict[psum-goal]

            my_dict[psum]+=1

        return count




        