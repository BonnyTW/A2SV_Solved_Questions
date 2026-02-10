class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        paired=list(sorted(zip((n for n in indices),(ch for ch in s))))
        print(paired)
        ans=""
        for p in paired:
            ans+=p[1]
        return ans


        
