class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
        res=[]
        
        
        def helper(n,l):
            
            if len(arr) == k:
                res.append(arr[:])
                return
            if  n>l:
                return

            arr.append(n)
            helper(n+1,l)
            arr.pop()
            helper(n+1,l)
            
        helper(1,n)

        return res