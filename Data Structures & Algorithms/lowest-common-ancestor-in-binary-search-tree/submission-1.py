class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited = []

        p_node = root
        while p_node:
            visited.append(p_node)
            if p_node.val == p.val: break
            if p_node.val < p.val:
                p_node = p_node.right
            else:
                p_node = p_node.left

        q_node = root
        i = 0
        while q_node:
            # We found our diverging node
            # visited[0].val is guaranteed to be the root

            # If the path of the 2nd TreeNode is greater than the 1st, we would get a list index out of range
            # it signifies that the paths diverged at the last node
            print(q_node.val)

            if i >= len(visited): return visited[i-1]

            if visited[i].val != q_node.val: 
                print("boom")
                return visited[i-1]

            i += 1
            if q_node.val == q.val: break
            if q_node.val < q.val:
                q_node = q_node.right
            else:
                q_node = q_node.left

        return visited[i-1]