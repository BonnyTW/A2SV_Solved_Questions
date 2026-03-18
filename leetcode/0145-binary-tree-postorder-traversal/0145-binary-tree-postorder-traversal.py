# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]

        def pos_or(root):
            if not root:
                return 
            pos_or(root.left)
            pos_or(root.right)
            ans.append(root.val)
        pos_or(root)
        return ans
        