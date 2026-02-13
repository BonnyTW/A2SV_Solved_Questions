class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        my_dict=defaultdict(int)
        rev=defaultdict(int)
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in my_dict:
                if s[i]!=my_dict[pattern[i]]:
                    return False
        
            elif pattern[i] not in my_dict and s[i] not in rev:
                my_dict[pattern[i]]=s[i]
                rev[s[i]]=pattern[i]
            else:
                return False

        return True


        
