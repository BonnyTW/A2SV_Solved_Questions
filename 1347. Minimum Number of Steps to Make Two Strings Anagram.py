class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scount=Counter(s)
        tcount=Counter(t)

        value=0
        for ch in tcount:
            if tcount[ch]<=scount[ch]:
                continue
            else:
                value+=tcount[ch]-scount[ch]
        return (value)
        
