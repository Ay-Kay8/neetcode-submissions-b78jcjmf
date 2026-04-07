class Solution:    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0
        
        def get_height(root):
            if not root:
                return 0

            curr_diameter = get_height(root.left) + get_height(root.right)
            self.max_diameter = max(self.max_diameter, curr_diameter)

            return max(get_height(root.left), get_height(root.right)) + 1
        
        get_height(root)
        
        return self.max_diameter