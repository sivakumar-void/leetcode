# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        u=[]
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            if root.val not in u:
                u.append(root.val)
            inorder(root.right)
        inorder(root)
        return len(u)==1
        