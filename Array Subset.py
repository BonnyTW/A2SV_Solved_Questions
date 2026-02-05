
from collections import Counter
class Solution:
    def isSubset(self, a, b):
        bcount=Counter(b)
        acount=Counter(a)
        for key in bcount:
            if key in acount:
                if bcount[key]>acount[key]:
                    return False
                else:
                    continue
            else:
                return False
        return True
            
        
        
    
    
    
            
