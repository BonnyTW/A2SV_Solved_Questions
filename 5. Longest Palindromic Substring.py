class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]!=s[j]:
                    continue
                else:
                    current=s[i:j+1]
                    if len(current)>len(longest) and current[::-1]==current:
                        longest=current
        return (longest)
                    
        
