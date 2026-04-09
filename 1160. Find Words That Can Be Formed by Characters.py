class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        charCounter=Counter(chars)
        for word in words:
            myd=Counter(word)
            for k in myd:
                if k in charCounter:
                    if myd[k]<=charCounter[k]:
                        continue
                    else:
                        break
                else:
                    break
            else:
                ans+=len(word)
        return (ans) 
                
        
