class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        count=defaultdict(list)
        
        
        for path in paths:
            totpath=path.split(" ")
            root=totpath[0]

            for n in totpath[1:]:
                name,content=n.split('.txt')
                count[content].append((root,name))
       
        
        ans=[]
        for k,v in count.items():
            tmp=[]
            if len(v)>1:
                for n in v:
                    tmp.append(n[0]+'/'+n[1]+'.txt')
                ans.append(tmp)
        return (ans)


