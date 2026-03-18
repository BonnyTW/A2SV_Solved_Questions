class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def f(l,r):
            if l==r:
                return nums[r]

            left=nums[l]-f(l+1,r)
            right=nums[r] - f(l,r-1)

            return max(left,right)
        return f(0,len(nums)-1) >=0
        