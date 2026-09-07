# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result=[]
        def inorder1(root1):
            if root1 is None:
                return 
            inorder1(root1.left)
            result.append(root1.val)
            inorder1(root1.right)
        def inorder2(root2):
            if root2 is None:
                return 
            inorder2(root2.left)
            result.append(root2.val)
            inorder2(root2.right)
        inorder1(root1)
        inorder2(root2)
        return sorted(result)
         
        