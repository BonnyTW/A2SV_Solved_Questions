class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=Counter(nums)

        for key,value in freq.items():
            if value>=2:
                return key
        
        
