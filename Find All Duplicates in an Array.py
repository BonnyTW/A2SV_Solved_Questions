class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        numCount=Counter(nums)
        for key in numCount:
            if numCount[key]==2:
                ans.append(key)
        return ans
