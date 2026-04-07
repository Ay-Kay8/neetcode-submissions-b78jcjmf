class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        index = 1

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if index == k:
                return curr.val
            index += 1
            curr = curr.right
        # return "Not found"