class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[0])
        merged = [points[0]]
        
        for s, e in points[1:]:
            if s <= merged[-1][1]:
                merged[-1][1] = min(e, merged[-1][1])
            else:
                merged.append([s, e])
        
        return len(merged)
