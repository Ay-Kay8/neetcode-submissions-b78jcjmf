# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            res.append(q[0].val) # peek
            # print(f"{[n.val for n in q]} len={len(q)}",  end=", ")
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return res