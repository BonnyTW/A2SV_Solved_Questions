class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dq = deque(matrix)  
        ans=[]

        while dq:
            
            for num in dq[0]:
                ans.append(num)
            dq.popleft()
            print(ans)
            
            for j in range(len(dq)):
                if dq[j]:
                    ans.append(dq[j][-1])
                    dq[j].pop()
            
            print(ans)
            

            if not dq:
                break

            for k in range(len(dq[-1])-1,-1,-1):
                ans.append(dq[-1][k])
            dq.pop()

            for j in range(len(dq)-1,-1,-1):
                if dq[j]:
                    ans.append(dq[j][0])
                    dq[j].pop(0)
        return (ans)

            

