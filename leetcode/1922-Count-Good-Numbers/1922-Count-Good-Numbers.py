class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x,n):
            if n==0:
                return 1
            half=power(x,n//2)

            if n%2:
                return (half*half*x)%(10**9 + 7)
            else:
                return (half*half)%(10**9 + 7)
        e_n=(n+1)//2
        o_n=n//2
        return (power(5,e_n)*power(4,o_n))%(10**9 + 7)