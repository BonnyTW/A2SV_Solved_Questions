class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        my_dict=Counter(s1+s2)
        for num in my_dict.values():
            if num%2:
                return -1

        count=Counter()
        for i in range(len(s1)):
            if s1[i]!=s2[i]: 
                count[s1[i]+s2[i]]+=1 
        res=0
        for value in count.values():
            if value%2:
                res+=((value//2)+1)
            else:
                res+=(value//2)
        return res
        

        

        
