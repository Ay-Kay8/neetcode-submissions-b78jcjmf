class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p:
            return not q
        if not q:
            return not p

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)