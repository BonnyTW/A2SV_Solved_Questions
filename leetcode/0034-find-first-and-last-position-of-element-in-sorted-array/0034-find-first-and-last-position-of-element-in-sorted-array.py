class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower(nums,target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def upper(nums,target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        lower_bound = lower(nums,target)
        upper_bound = upper(nums,target)

        if lower_bound == upper_bound:
            return [-1,-1]
        return [lower_bound,upper_bound-1]


        