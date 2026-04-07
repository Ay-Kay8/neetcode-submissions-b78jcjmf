# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        curr_diameter = self.getHeight(root.left) + self.getHeight(root.right)

        left_diameter = self.helper(root.left)
        right_diameter = self.helper(root.right)

        return max(curr_diameter, left_diameter, right_diameter)

    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left) + 1, self.getHeight(root.right) + 1)
           