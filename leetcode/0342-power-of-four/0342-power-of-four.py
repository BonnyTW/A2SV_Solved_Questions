class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        possible = False

        if n==1 or n==4:
            return True

        while n > 4:
            n/=4

        if n==4:
            return True
        else:
            return False
        
            
        