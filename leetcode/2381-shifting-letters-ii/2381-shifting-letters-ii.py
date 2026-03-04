class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
        # [0,1,2]

        # s = "dztz", shifts = [[0,0,0],[1,1,1]]
        # [-1,1,0,0]

        psum=[0]*(len(s)+1)
        ans=[]

        for f,e,d in shifts:
            if d == 0:
                psum [f] -= 1
                psum[e+1] += 1
            else:
                psum [f] += 1
                psum[e+1] -= 1
        
        for i in range(1,len(psum)):
            psum[i] += psum[i-1] 
        print(psum)



        for i in range(len(s)):
            ch = ((ord(s[i])-97)+psum[i])%26
            ans.append(chr(ch+97))

        return ''.join(ans)




            




    


