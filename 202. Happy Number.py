class Solution:
    def isHappy(self, n: int) -> bool:

        def splitsum(n):
            chsqr=0
            for ch in str(n):
                chsqr+=int(ch)**2
            return chsqr 

        seen=set()
        
        x=splitsum(n)
        while x!=1:
            if x in seen:
                return False
            else:
                seen.add(x)
                x=splitsum(x)
        return True

                
        
