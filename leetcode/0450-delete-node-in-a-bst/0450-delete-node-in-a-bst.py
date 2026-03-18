# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root,key):
            if not root:
                return 
            if key>root.val:
                root.right=helper(root.right,key)
            elif key<root.val:
                root.left=helper(root.left,key)

            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                curr=root.right
                while curr.left:
                    curr=curr.left
                root.val=curr.val
                root.right = helper(root.right,curr.val)
                
            return root
        return helper(root,key)
        
        