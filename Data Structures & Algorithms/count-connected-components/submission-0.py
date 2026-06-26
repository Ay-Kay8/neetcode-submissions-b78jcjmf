from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = dict((i, []) for i in range(n))
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()

        # no need to avoid parent since we'll have visited set
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        components = 0
        for node in graph:
            if node not in visited:
                components += 1
                dfs(node)

        return components