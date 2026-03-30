class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def power(x,n):
            if x==0:return 0
            if n==0:return 1
        
            half=power(x,n//2)
            if n%2:
                return (half*half*x)%((10**9)+7)
            else:
                return (half*half)%((10**9)+7)

        return (power(5,(n+1)//2)*power(4,n//2))%((10**9)+7)



        
        
        