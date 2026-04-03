class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in  nums:
            idx = bisect_left(arr,num)
            if len(arr) == idx:
                arr.append(num)
            else:
                arr[idx] = num
                
        return len(arr)