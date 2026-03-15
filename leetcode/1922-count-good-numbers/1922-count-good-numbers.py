class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        e_c=(n+1)//2
        o_c=n//2
        

        return pow(5,e_c,10**9+7)*pow(4,o_c,10**9+7)%(10**9+7)
        