class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x

        max_n=-1
        while low <= high:
            mid= (low+high)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid+1
                max_n=mid
            else:
                high=mid-1
        return max_n

        
        