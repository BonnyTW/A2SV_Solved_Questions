class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        arr=s.copy()
        def helper(i):
            if i == len(s):
                return
            helper(i+1)
            arr[(len(s)-1)-i]=s[i]
        helper(0)
        s[:]=arr

            
        
        