class Solution:    
    def findUnion(self, a, b):
        res=a+b
        res=list(set(res))
        res.sort()
        return (res)
