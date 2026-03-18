# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]

        def preor(r):
            if r:
                preor(r.left)
                ans.append(r.val)
                
                preor(r.right)
        preor(root)
        return ans
        