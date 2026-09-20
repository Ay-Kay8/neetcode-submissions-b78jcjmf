class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque()
        res = []

        queue.append(root)
        while queue:

            res.append(queue[-1].val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return res