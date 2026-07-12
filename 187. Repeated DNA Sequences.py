class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        seen = set()
        left = 0

        while left < len(s) - 9:
            sub = s[left:left + 10]
            if sub in seen:
                ans.append(sub)
            seen.add(sub)
            left += 1
        
        return list(set(ans))

        

        
