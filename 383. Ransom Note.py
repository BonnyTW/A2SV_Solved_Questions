class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rs_Count=Counter(ransomNote)
        mgz_Count=Counter(magazine)

        for ch in set(ransomNote):
            if rs_Count[ch]>mgz_Count[ch]:
                return False
        return True
        
