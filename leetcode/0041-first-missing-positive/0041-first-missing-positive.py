class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 1

        while ans < (2**31) - 1:
            if ans not in nums:
                return ans
            ans += 1


        