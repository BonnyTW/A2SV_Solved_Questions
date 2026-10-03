class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        ans = []
        prev = 0
        for num in spaces:
            ans.append(s[prev:num])
            prev = num

        ans.append(s[prev:])
        
        return ' '.join(ans)
        
