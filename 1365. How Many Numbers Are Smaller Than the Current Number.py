class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # counting sort
        nums2 = nums[:]
        max_num=max(nums2)
        counting=[0]*(max_num+1)

        for num in nums2:
            counting[num]+=1

        target=0

        for idx,val in enumerate(counting):
            for i in range(val):
                nums2[target]=idx
                target+=1
        print(nums2)
        

        mydict={}
        for i in range(len(nums2)):
            if nums2[i] not in mydict:
                mydict[nums2[i]]=i
        print(mydict)
        ans=[]
        for i in range(len(nums)):
            ans.append(mydict[nums[i]])
        return ans
        
