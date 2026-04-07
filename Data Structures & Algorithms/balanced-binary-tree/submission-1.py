class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        is_balanced = self.isBalanced(root.left) and self.isBalanced(root.right)

        return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and is_balanced

    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1