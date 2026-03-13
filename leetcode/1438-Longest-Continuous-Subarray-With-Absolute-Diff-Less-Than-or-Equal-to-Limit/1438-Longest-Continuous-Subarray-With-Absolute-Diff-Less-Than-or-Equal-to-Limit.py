class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        md_q=deque()
        mi_q=deque()
        left=0

        res=0

        for i in range(len(nums)):
            while mi_q and nums[mi_q[-1]] > nums[i]:
                mi_q.pop()
            while md_q and nums[md_q[-1]] < nums[i]:
                md_q.pop()
            mi_q.append(i)
            md_q.append(i)

            if nums[md_q[0]] - nums[mi_q[0]] > limit:
                if nums[mi_q[0]]==nums[left]:
                    mi_q.popleft()
                if nums[md_q[0]]==nums[left]:
                    md_q.popleft()
                left+=1
            res=max(res,i-left+1)
        return res