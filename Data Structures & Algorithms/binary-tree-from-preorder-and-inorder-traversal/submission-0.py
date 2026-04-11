class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # 1:(mid + 1) is the range of preorder that belongs in the left subtree
        # given to use by the number of values on the left side of mid in inorder         
        root.left = self.buildTree(preorder[1:(mid + 1)], inorder[:mid])
        root.right = self.buildTree(preorder[(mid + 1):], inorder[(mid + 1):])

        return root