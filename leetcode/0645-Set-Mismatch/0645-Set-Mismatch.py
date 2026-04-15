class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        dif = set(nums)
        max_n = max(nums)

        i = 1
        miss = 0
        dup = 0
        while i <= max_n:
            if i not in dif:
                miss = i
                break
            i += 1
        for num in nums:
            count[num] -= 1
            if count[num] == 1:
                dup = num
        if miss == 0:
            miss = i
        return [dup,miss]