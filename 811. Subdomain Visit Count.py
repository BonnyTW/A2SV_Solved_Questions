class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for tdomain in cpdomains:
            count,domain=tdomain.split()
            count=int(count)
            
            fragment=domain.split('.')
            for i in range(len(fragment)):
                counts['.'.join(fragment[i:])]+=count
        ans=[]
        for key,value in counts.items():
            ans.append(str(value)+' '+key)
        return ans 
        
