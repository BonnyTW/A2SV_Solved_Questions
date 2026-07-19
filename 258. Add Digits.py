class Solution:
    def addDigits(self, num: int) -> int:
        
        def helper(n):
            if len(n) == 1:
                return int(n)
            
            ans = sum(int(x) for x in n)
            return helper(str(ans))
        
        return helper(str(num))
        
