class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)

        ans = []
        for num in order:
            if num in friends:
                ans.append(num)
        
        return ans
