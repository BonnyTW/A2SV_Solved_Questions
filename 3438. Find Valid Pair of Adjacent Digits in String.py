from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        ans = ''
        counter = Counter(s)
        print(counter)
        
        for i in range (1,len(s)):
            if counter[s[i-1]]!=counter[s[i]]:
                if counter[s[i-1]] == int(s[i-1]) and  counter[s[i]] == int(s[i]):
                    return s[i-1]+s[i]
        return ans
