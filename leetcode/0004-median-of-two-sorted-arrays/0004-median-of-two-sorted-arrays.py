class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        nums.extend(nums1[i:])
        nums.extend(nums2[j:])



        mid = (len(nums) - 1) // 2

        if len(nums) % 2:
            return nums[mid] 
        else:
            return (nums[mid] + nums[mid + 1] ) / 2