# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        val = root.val

        dq = deque([root])

        while dq:
            node = dq.popleft()

            if node.val != val:
                return False

            if node.right:
                dq.append(node.right)

            if node.left:
                dq.append(node.left)
            
        return True