class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def pow4(n):
            if n == 0:
                return False
            if n == 1:
                return True

            return pow4(n/4)
        
        return pow4(n)

        
