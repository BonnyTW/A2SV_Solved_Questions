class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]

        count=0
        for dir in logs:
            if dir=='./':
                continue
            elif dir!='../':
                count+=1
            else:
                count-=1
                if count<0:
                    count=0
        return count if count>0 else 0
            
        