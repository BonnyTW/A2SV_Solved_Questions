class Solution:
    def isValid(self, s: str) -> bool:
        mydict={')':'(','}':'{',']':'['}

        stack=[]
        
        for ch in s:
            if ch not in mydict:
                stack.append(ch)
               
            else:
                if not stack:
                    return False
                    
                if stack[-1]!=mydict[ch]:
                    return False
                stack.pop()
                
        if len(stack)==0:
            return True
        return False

        