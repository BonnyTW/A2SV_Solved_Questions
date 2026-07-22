class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1

        ans = 0
        while j < len(s):
            ans += abs(ord(s[j]) - ord(s[i]))
            i += 1
            j += 1
        
        return ans

        
