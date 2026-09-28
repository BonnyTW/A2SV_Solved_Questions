class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0

        stack = []

        for ch in s:
            if ch == ')':
                max_count = max(max_count,len(stack))
                stack.pop()
            elif ch == '(':
                stack.append(ch)
            else:
                continue
        
        return max_count

                


        
