class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                mid = []
                while stack and stack[-1] != '(':
                    mid.append(stack.pop())
                
                if stack:
                    stack.pop()
                stack.extend(mid)
        
            else:
                stack.append(ch)
        
        return ''.join(stack)
