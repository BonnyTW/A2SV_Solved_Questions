class Solution:
    def frequencySort(self, s: str) -> str:
        count=sorted(Counter(s).items(),key=lambda x:x[1],reverse=True)
        ans=''
        for pair in count:
            ans+=pair[0]*pair[1]
        return (ans)

        
