class Solution:
    def magicalString(self, n: int) -> int:
        s = [1,2,2]

        count = 1
        num = 1

        if n <= 3:
            return 1
        
        i = 2
        
        while len(s) < n:
            for _ in range(s[i]):
                s.append(num)

                if num == 1:
                    count += 1
                
                if len(s) == n:
                    break
            num = 3 - num

            i += 1
        
        return count
        
        
        
