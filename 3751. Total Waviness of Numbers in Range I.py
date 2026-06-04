class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1,num2 + 1):
            ch = str(i)
            for c in range(len(ch) - 2):
                if (ch[c] < ch[c+1] > ch[c+2]) or (ch[c] > ch[c+1] < ch[c+2]):
                    count += 1
        return count


        
