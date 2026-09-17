from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append((p, q))
        while queue:
            root1, root2 = queue.popleft()

            if root1 and root2:
                queue.append((root1.left, root2.left))
                queue.append((root1.right, root2.right))

                if root1.val != root2.val:
                    return False
            elif not root1 and not root2:
                continue
            else:
                return False

        return True