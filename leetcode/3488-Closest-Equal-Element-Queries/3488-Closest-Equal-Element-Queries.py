class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        indexes = defaultdict(list)
        ans = []

        for idx,val in enumerate(nums):
            indexes[val].append(idx)
        

        for query in queries:
            num = nums[query]
            arr = indexes[num]

            if len(arr) == 1:
                ans.append(-1)
                continue
            
            i = bisect_left(arr,query)

            left = arr[i - 1] if i > 0 else arr[-1]
            right = arr[i + 1] if i + 1 < len(arr) else arr[0]

            def dist(a,b):
                forw = abs(a-b)
                return min(forw,len(nums) - forw)
            
            ans.append(min(dist(query,left),dist(query,right)))
        return ans