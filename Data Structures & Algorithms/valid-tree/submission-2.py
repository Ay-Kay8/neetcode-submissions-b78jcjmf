from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = dict([(i, []) for i in range(n)])
        for root, child in edges:
            graph[root].append(child)
            graph[child].append(root) # since this is an undirected graph

        # start off with a set with the first parent (0)
        visited = set()
        # 1. No cycles check
        def has_cycles(parent, node):
            visited.add(node)

            for child in graph[node]:
                if child == parent: # since this is undirected, skip if child came from parent
                    continue
                if child in visited:
                    return True

                if has_cycles(node, child):
                    return True

            return False

        # I tried doing list(visited) == list(graph.keys()) but it doesn't work since sets are unordered
        return not has_cycles(-1, 0) and len(visited) == n