class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount=sorted(Counter(nums).items(),key=lambda x:x[1],reverse=True)
        return [numcount[i][0] for i in range(k)]


        
