class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        val = self.countAndSay(n-1)
        ans = []
        i = 0
        j = 0
        count = 0
        while j < (len(val)):
            if val[i] == val[j]:
                count += 1
            else:
                ans.append(str(count))
                ans.append(val[i])
                i = j
                count = 1            
            j += 1
        # for last part
        ans.append(str(count))
        ans.append(val[i])
            
        return ''.join(ans)