class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        my_dict=Counter({0:-1})

        psum=0
        for i,num in enumerate(nums):
            psum+=num
            if psum%k in my_dict:
                if i-my_dict[psum%k]>=2:
                    return True
            else:
                my_dict[psum%k]=i
        return False

        