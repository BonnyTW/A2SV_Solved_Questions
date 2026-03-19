# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def helper(root,parent, grandpa):
            if not root:
                return 
            if grandpa and grandpa.val % 2 == 0:
                self.ans += root.val
            
            helper(root.left,root,parent)
            helper(root.right,root,parent)
            
        helper(root,None,None)
        return self.ans