# Version 1
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # node, curr_max
        stack = [(root, root.val)]
        count = 0 # ** Start at 0 instead

        while stack: 
            # curr_max is 
            node, curr_max = stack.pop()

            if node.val >= curr_max:
                count += 1

            curr_max = max(node.val, curr_max)

            if node.left:
                stack.append((node.left, curr_max))
            if node.right:
                stack.append((node.right, curr_max))

        return count