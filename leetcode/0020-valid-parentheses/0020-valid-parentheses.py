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
                prev=stack.pop()
                if prev!=mydict[ch]:
                    return False
                
        if len(stack)==0:
            return True
        return False

        