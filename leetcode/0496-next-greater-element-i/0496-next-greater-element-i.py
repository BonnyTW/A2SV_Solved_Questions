class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            j=0
            
            while j<len(nums2) and nums2[j]!=nums1[i]:
                j+=1

            j+=1
            while j<len(nums2):
                if nums2[j]>nums1[i]:
                    ans.append(nums2[j])
                    break
                j+=1
            else:
                ans.append(-1)
        return ans
        