class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        #  put max_num at 0 and then flip it(to its postion)
        #  3 2 4 1
        #  4 2 3 1 ...    3
        #  1 3 2 4 ...    4
        #  3 1 2 4 ...    2
        #  2 1 3 4 ...    3
        #  1 2 3 4 ...    2

        i=len(arr)
        ans=[]
        while i >= 0:
            # choose max num
            if len(arr[:i])>=1:
                max_n=max(arr[:i])
            
            # place max_num at 0 
            if arr!=sorted(arr):
                idx_max=arr.index(max_n)
                if idx_max!= 0:
                    ans.append(idx_max+1)
                    arr[:idx_max+1]=reversed(arr[:idx_max+1])
                print(arr)
            # place the max_num at its position (by plipping)
            if arr!=sorted(arr):
                arr[:i]=reversed(arr[:i])
                ans.append(i)
                print(arr)
            i-=1
        return (ans)



        
        
