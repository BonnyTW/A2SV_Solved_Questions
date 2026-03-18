# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(root):
            if not root:
                return TreeNode(val)
            if val>root.val:
                root.right=search(root.right)
            else:
                root.left=search(root.left)
            return root
        return search(root)
            
            

        