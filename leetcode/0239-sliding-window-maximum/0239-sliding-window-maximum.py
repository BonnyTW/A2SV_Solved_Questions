class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        md_q=deque()
        ans=[]

        for i in range (len(nums)):
            while md_q and nums[md_q[-1]] < nums[i]:
                md_q.pop()
            
            if md_q and md_q[0] <= i - k:
                md_q.popleft()
            
            md_q.append(i)

            if i >= k-1:
                ans.append(nums[md_q[0]])
        return ans
        