class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        org=strs[0]
        ans=""
        for word in strs[1:]:
            i=0
            while i<len(word) and i<len(org) and word[i]==org[i]:
                i+=1
            org=org[:i]

        return org
            



        
