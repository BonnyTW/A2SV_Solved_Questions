class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        notall=False
        for i in range(left,right+1):
            j=0
            while j<len(ranges) and not(ranges[j][0]<=i<=ranges[j][1]):
                j+=1
            if j>=len(ranges):
                return False
        return True
             


        
