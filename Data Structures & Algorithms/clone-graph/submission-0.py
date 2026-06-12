
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__(self):
        return f"Node val={self.val}, neighbors={[n.val for n in self.neighbors]}"

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        queue = deque([node])

        # Debugging
        adj_list = []

        # real node: deep clone
        clones = {}

        while queue:
            
            curr_node = queue.popleft()
            if curr_node not in clones:
                clones[curr_node] = Node(curr_node.val)

            # Debugging
            adj_list.append([v.val for v in curr_node.neighbors])

            for neighbor in curr_node.neighbors:

                if neighbor not in clones:
                    queue.append(neighbor)

                    # Add neighbor to the clones
                    clones[neighbor] = Node(neighbor.val)

                # Link them together (neighbor goes in curr_node)
                clones[curr_node].neighbors.append(clones[neighbor])

        return clones[node]
        # return adj_list
