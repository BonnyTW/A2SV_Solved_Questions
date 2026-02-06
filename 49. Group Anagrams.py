class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        mydict={}
        for word in strs:
            key=''.join(sorted(word))
            ans=[word]
            if key not in  mydict:
                mydict[key]=ans
            else:
                mydict[key].append(word)
        for value in mydict.values():
            res.append(value)
        return res




