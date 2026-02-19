class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        # [9,8,7,6,5,1,2,3,4]-> 9,8,7,6,5,4,3,2,1
        #{9,8,3}, {7,6,2}, {5,4,1} --------> 8 + 6 + 4 =18

        #[1,2,3,4,5,6,7,8,9,10,11,12]
        #{12,11,4}  {10,9,3} {8,7,2}  {6,5,1}------>11+ 9+ 7 +5 = 32

       # piles = [2,4,1,2,7,8]->  [8,7,4,2,2,1]
        #{8,7,2}    {4,2,1}------------------------> 7 + 2 = 9

        
        k=len(piles)//3
        piles=sorted(piles,reverse=True)
        print(piles)
        max_num=0
        for i in range(1,len(piles)-k,2):
            max_num+=piles[i]
        return max_num

       

        
