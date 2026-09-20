class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque()
        res = []

        queue.append(root)
        while queue:

            level_size = len(queue)

            for i in range(level_size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

                if i == level_size - 1:
                    res.append(curr.val)

        return res