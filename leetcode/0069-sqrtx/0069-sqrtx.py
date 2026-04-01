class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        if x==1:
            return 1

        flag = False

        while left < right:
            mid = (left + right) // 2

            if mid*mid == x:
                flag =True
                return mid

            if mid*mid > x:
                right = mid
            else:
                ans = mid
                left = mid + 1

        if not flag:
            return ans


        
        