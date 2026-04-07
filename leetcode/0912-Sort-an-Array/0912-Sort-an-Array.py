class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l_h,r_h):
            l = 0
            r = 0
            arr=[]
            while l < len(l_h) and r < len(r_h):
                if l_h[l] <= r_h[r]:
                    arr.append(l_h[l])
                    l += 1
                else:
                    arr.append(r_h[r])
                    r += 1
            arr.extend(l_h[l:])
            arr.extend(r_h[r:])

            return arr

        def mergeSort(left,right,arr):
            if left == right:
                return [nums[left]]
            mid = (left + right) // 2

            left_h = mergeSort(left,mid,arr)
            right_h = mergeSort(mid+1,right,arr)

            return merge(left_h,right_h)
        
        return mergeSort(0,len(nums)-1,nums)