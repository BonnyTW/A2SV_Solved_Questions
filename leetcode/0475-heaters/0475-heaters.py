from bisect import bisect_left
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans=0
        heaters.sort()
        for house in houses:
            left = 0
            right = len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] >= house:
                    right = mid - 1
                else:
                    left = mid + 1
                
            idx = left
            
            left_dis = float('inf')
            if idx > 0:
                left_dis = house - heaters[idx -1]
            
            right_dis = float('inf')
            if idx < len(heaters):
                right_dis = heaters[idx] - house

            closest = min (left_dis,right_dis)
            ans = max(ans,closest)

        return ans
        