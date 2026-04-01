class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        if x==1:
            return 1

        while left < right:
            mid = (left + right) // 2

            if mid*mid == x:
                return mid

            if mid*mid > x:
                right = mid
            else:
                ans = mid
                left = mid + 1

        return ans


        
        