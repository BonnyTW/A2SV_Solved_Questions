class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        my_dict = defaultdict()
        for k,v in knowledge:
            my_dict[k] = v
        
        ans = []

        i = 0
        while i < len(s):
            if s[i] != '(':
                ans.append(s[i]) 
                i += 1
                continue
            i += 1
            key = ''
            while i< len(s) and s[i] != ')':
                key += s[i]
                i += 1
            i += 1
            print(key)
            ans.append(my_dict.get(key, "?"))
            
        return ''.join(ans)
            
        
        


        
