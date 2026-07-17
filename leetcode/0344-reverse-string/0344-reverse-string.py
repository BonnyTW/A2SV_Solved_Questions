class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Iterative
        '''
        i = 0
        j = len(s) - 1

        while i <= j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        '''

        # Recursive
        def helper(left,right):
            if left >= right:
                return
            
            s[left],s[right] = s[right],s[left]
            helper(left + 1,right - 1)

        helper(0,len(s) - 1)
        
