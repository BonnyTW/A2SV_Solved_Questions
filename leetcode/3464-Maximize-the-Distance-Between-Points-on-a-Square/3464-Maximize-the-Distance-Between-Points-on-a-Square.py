from typing import List
from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        
        # Step 1: convert (x, y) → position
        def get_pos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 2 * side + (side - x)
            else:
                return 3 * side + (side - y)

        pos = sorted(get_pos(x, y) for x, y in points)
        n = len(pos)
        perimeter = 4 * side

        #  REMOVE pos_extended (not needed anymore)

        # Step 3: optimized check function
        def can(d):
            for start_idx in range(n):
                start = pos[start_idx]
                current = start
                
                # enforce circular constraint
                max_allowed = start + perimeter - d

                for _ in range(k - 1):
                    # jump directly to next valid point
                    next_idx = bisect_left(pos, current + d)
                    
                    #  fail conditions
                    if next_idx == n or pos[next_idx] > max_allowed:
                        break
                    
                    current = pos[next_idx]
                else:
                    # successfully picked k points
                    return True

            return False

        # Step 4: binary search
        left, right = 1, side   
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans