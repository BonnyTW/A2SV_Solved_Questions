class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        app=""
        for num in nums:
            app+=str(num)
        return [int(ch) for ch in app]
        
