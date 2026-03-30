class Solution:
    def countGoodNumbers(self, n: int) -> int:
        n_e=(n+1)//2
        n_o=n//2

        return (pow(5,n_e,(10**9)+7)*pow(4,n_o,(10**9)+7))%((10**9)+7)



        
        
        