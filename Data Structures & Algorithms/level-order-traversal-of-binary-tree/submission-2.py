class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # So at one point, the queue will only have the values belonging to one level
        # How do we know when that is?
        q = deque([root])
        res = []

        curr = root
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            res.append(level)
            level = []
        return res