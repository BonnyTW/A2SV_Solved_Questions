class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i=0
        while i < (len(citations)):
            while i < len(citations) and citations[i] < len(citations) - i:
                i+=1
            return len(citations) -i
                

            
        