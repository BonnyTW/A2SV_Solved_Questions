class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]

        for i in range(1, len(nums)):
            while stack and stack[-1] + nums[stack[-1]] < i:
                stack.pop()

            if not stack:
                return False

            stack.append(i)

        return True
