class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        md_s=[]

        for i in range(len(temperatures)):
            while md_s and temperatures[md_s[-1]]<temperatures[i]:
                prev=md_s.pop()
                ans[prev]=i-prev
            md_s.append(i)
        return ans


        