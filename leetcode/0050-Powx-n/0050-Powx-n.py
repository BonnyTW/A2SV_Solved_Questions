class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(n):
            if n == 0:
                return 1
            
            if n < 0:
                return 1 / power(-1*n)
            half = power(n//2)

            if n % 2:
                return half * half * x
            return half * half
        
        return power(n)
        
