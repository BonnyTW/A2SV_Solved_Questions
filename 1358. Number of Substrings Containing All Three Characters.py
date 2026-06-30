class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0

        my_dict = {'a':0,'b':0,'c':0}
        freq = Counter()

        
        for right in range(len(s)):
            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                count += len(s) - right 
                freq[s[left]] -= 1
                left +=1 
        
        return count

            


        
