class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #[-2,1,-3,4,-1,2,1,-5,4] [3,6]
        #[0,-2,-1,-4,0,-1,1,2,-3,1]=2-(-4)=6

        #[5,4,-1,7,8]
        #[0,5,9,8,15,23]

        #[0,-1]->[0,-1]

        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        print(prefix)

        largest=float('-inf')
        minnum=float('inf')

        for num in prefix:
            largest=max(largest,num-(minnum))
            if num < minnum:
                minnum=num
            
            
        return (largest)