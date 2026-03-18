# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=[]

        def search(root):
            if not root:
                return
            if root.val == val:
                return root
            left=search(root.left)
            right=search(root.right)
            if left:
                return left
            return right
        
        return search(root)
        
        
            
            
            

        