class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                res=[]
                while stack and stack[-1]!='[':
                    res.append(stack.pop())
                stack.pop()
                
                res=''.join(res[::-1])

                num=[]

                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num = int(''.join(num[::-1]))

                stack.append(res*num)
        return (''.join(stack))
            


            
        