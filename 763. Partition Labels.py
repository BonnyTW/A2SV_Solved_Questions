class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=Counter(s)

        
        cur=set() 
        ans=[]
        prev=0
        for i in range (len(s)):
            cur.add(s[i])
            if count[s[i]]!=0:
                count[s[i]]-=1
                if count[s[i]]==0:
                    cur.discard(s[i])

            if len(cur)==0:
                if prev==0:
                    ans.append(i+1)
                    prev=i+1
                else:
                    ans.append(i-prev+1)
                    prev=i+1
                
        return ans
            

        
