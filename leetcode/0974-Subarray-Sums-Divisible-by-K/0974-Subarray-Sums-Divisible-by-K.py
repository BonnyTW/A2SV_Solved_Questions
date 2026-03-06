class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # [4,5,0,-2,-3,1]---> [0,4,9,9,7,4,5]-->[0,4,4,4,2,4,0]

        #{0:2,4:4,2:1}c=1+2+3+1=7

        my_dict=Counter()

        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        print(prefix)

        for i in range(len(prefix)):
            prefix[i]=prefix[i]%k
        
        count=0
        for num in prefix:
            if num in my_dict:
                count+=my_dict[num]
            my_dict[num]+=1
        return (count)