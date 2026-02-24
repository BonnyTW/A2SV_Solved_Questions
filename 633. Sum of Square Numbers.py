class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        j=int(math.sqrt(c))
        i=0

        while i<= j:
            if i*i+j*j==c:
                return True
            elif  i*i+j*j<c:
                i+=1
            else:
                j-=1
        return False

        
