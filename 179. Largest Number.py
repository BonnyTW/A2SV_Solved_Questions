class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i,num in enumerate(nums):
            nums[i]=str(num)
        
        def custom(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(custom))
        
        if ''.join(set(nums))=='0':
            return '0'
        
        return ''.join(nums)

        
