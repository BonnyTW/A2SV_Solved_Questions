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


''' 
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        my_dict = {')':'(','}':'{',']':'['}

        for ch in s:
            if ch not in my_dict:
                stack.append(ch)
                continue
            
            if stack and stack[-1] == my_dict[ch]:
                stack.pop()
            else:
                return False

        print(stack)

        if stack:
            return False
        return True
        
'''
