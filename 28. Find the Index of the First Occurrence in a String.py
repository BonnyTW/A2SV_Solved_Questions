class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i=0
        for j in range (len (haystack)-len(needle)+1):
            while i< len(needle) and needle[i]==haystack[j+i]:
                i+=1
            if i==len(needle):
                return j
            
            else:
                i=0
        return -1
