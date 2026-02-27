class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        count=0
        
        l_near =0
        l_far=0
        right=0
        distinict=Counter()

        while right < len(nums):
            distinict[nums[right]]+=1
            while len(distinict)>k:
                distinict[nums[l_near]]-=1
                if distinict[nums[l_near]]==0:
                    del distinict[nums[l_near]]
                l_near+=1
                l_far=l_near

            while distinict[nums[l_near]]>1:
                distinict[nums[l_near]]-=1
                l_near+=1


            if len(distinict)==k:
                count += l_near - l_far + 1
            right+=1
        return count




        
