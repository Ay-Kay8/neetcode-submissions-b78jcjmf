class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # root, lower bound, upper bound
        stack = [(root, float('-inf'), float('inf'))]


        while stack:
            curr, lower, upper = stack.pop()

            if curr.left:
                if not (lower < curr.left.val < curr.val):
                    return False
                stack.append((curr.left, lower, curr.val))
                # print(f"curr.left={curr.left.val}, lower={lower}, upper={curr.val}" )

            if curr.right:
                if not (curr.val < curr.right.val < upper):
                    return False
                stack.append((curr.right, curr.val, upper))
                # print(f"curr.right={curr.right.val}, lower={curr.val}, upper={upper}" )

        return True