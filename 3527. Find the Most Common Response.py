class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count=defaultdict(int)

        for response in responses:
            for res in set(response):
                count[res]+=1
              
        max_freq = max(count.values())
        ans = []
        for key in count:
            if count[key]==max_freq:
                ans.append(key)
        ans.sort()
        print(ans)
        return (ans[0])
        
        
