class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #[1,1,1]

        # 1+1=2, 1+1=2
        #[0,1,2,3]
        #[1,2,3]-> [0,1,3,6]
        #[1,2,3,3]-> [0,1,3,6,9]

        #{0:1,1:1,3:1,6:1,9:1}
        #count=3

        my_dict=Counter()

        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        print(prefix)
        count=0
        for num in prefix:
            if num-k in my_dict:
                count+=my_dict[num-k]
            my_dict[num]+=1
        print(my_dict)
        return count
            
            
        