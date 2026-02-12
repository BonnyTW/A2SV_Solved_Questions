class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for num in set(nums1):
            if num in set(nums2):
                ans.append(num)
        return ans
