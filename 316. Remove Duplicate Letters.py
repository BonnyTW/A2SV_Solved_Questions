class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()

        stack = []
        count = Counter(s)

        for ch in s:
            if ch in seen:
                count[ch] -= 1
                continue

            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(ch)
            seen.add(ch)

            count[ch] -= 1
        
        return ''.join(stack)
        
