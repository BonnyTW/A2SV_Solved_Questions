class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0

        for num in nums:
            if num - 1 in freq:
                count = max(count,freq[num] + freq[num - 1])
        return count

        
