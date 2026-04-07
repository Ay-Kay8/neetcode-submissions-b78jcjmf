class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): # -> (bool, int):
            if not root:
                return True, 0
            
            left_is_balanced, left_height = dfs(root.left)
            right_is_balanced, right_height = dfs(root.right)

            diff = abs(left_height - right_height)

            root_is_balanced = left_is_balanced and right_is_balanced and diff <= 1
            root_height = max(left_height, right_height)
            return root_is_balanced, root_height + 1
            
        balanced, height = dfs(root)
        return balanced
            