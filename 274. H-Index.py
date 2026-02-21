class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        print(citations)
        size=len(citations)
        
        if set(citations)=={0,}:
            return 0


        i=0
        while i <size:
            if citations[i]>=size-i:
                return size - i
            i+=1


            
        
