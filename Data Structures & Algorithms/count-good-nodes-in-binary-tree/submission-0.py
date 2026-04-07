class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # node, curr_max
        stack = [(root, root.val)]
        nb_good_nodes = 1

        while stack: 
            print(f"{[(n.val, v) for (n, v) in stack]}")
            curr, prev_max = stack.pop()

            if curr.left:
                curr_max = max(prev_max, curr.left.val)
                stack.append((curr.left, curr_max))

                print(f"left: {curr_max} >= {prev_max}")
                if curr.left.val >= prev_max:
                    nb_good_nodes += 1

            if curr.right:
                curr_max = max(prev_max, curr.right.val)
                stack.append((curr.right, curr_max))

                print(f"right: {curr_max} >= {prev_max}")
                if curr.right.val >= prev_max:
                    nb_good_nodes += 1

            print(nb_good_nodes)

        return nb_good_nodes