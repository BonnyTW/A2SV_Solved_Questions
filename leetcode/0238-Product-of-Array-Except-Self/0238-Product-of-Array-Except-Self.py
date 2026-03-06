import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 24
        # [1,2,3,4]---->  [24,12,8,6]

        # 0
        # [-1,1,0,-3,3]---->[0,0,9,0,0] if c(0)==1

        # 0
        #[-1,1,0,-3,0,3]----> [0,0,0,0,0,0]

        zeroCount=nums.count(0)
        tot=math.prod(nums)
        ans=[]
        pw0=1

        if zeroCount==1:
            for num in nums:
                if num !=0:
                    pw0*=num 
            for num in nums:
                if num==0:
                    ans.append(pw0)
                else:
                    ans.append(0)
            
        elif zeroCount>1:
            ans=[0]*len(nums)

        else:
            for num in nums:
                ans.append(tot//num)
        return (ans)