# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p:
                return not q
            
            if not q:
                return not p
            
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
        queue = deque([root])

        while queue:
            visited = queue.popleft()

            if isSameTree(visited, subRoot):
                return True

            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)
            
        return False
        