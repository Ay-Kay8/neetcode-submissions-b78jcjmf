# At every node, we call isSameTree on it, so time complexity is O(m * n)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p:
                return not q
            
            if not q:
                return not p
            
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)            
        
        # Empty subtree is a subtree of all
        if not subRoot:
            return True
        
        # If root is None and subRoot isn't (you don't need the "and subRoot")
        if not root and subRoot:
            return False

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
