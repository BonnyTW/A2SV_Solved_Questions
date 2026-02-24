class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        prev_s=skill[i]+skill[j]
        ans=0
        while i < j:
            if skill[i]+skill[j]==prev_s:
                ans+=(skill[i]*skill[j])
            else:
                return -1
            i+=1
            j-=1
        return ans
        
        
