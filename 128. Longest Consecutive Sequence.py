class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount=0
        seen=set(nums)
        for num in seen:
            if num-1 in seen:
                continue 
            cur=num
            count=0
            while num in seen:
                count+=1
                num+=1
            maxcount=max(count,maxcount)
        return maxcount




        
