class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_n = max(nums)
        min_n = min(nums)

        def gcd(min_n,max_n):
            if max_n == 0:
                return min_n
            return gcd(max_n,min_n % max_n)

        return gcd(min_n,max_n)
        
