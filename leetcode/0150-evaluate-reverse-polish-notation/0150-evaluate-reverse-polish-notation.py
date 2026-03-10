class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                if stack:
                    ans=0
                    first=stack.pop()
                    second=stack.pop()
                    if ch =='+':
                        ans=first+second
                    elif ch =='-':
                        ans=second-first
                    elif ch =='*':
                        ans=first*second
                    elif ch =='/':
                        ans=int(second/first)
                    stack.append(ans)
        return (stack[0])
                    


        