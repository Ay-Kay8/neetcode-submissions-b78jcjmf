class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 1. create graph
        graph = dict([(i, []) for i in range(numCourses)])
        for destination, source in prerequisites:
            graph[source].append(destination)

        count = 0
        for val in graph.values():
            if len(val) == 0:
                count += 1

        # 2. DFS algorithmn
        visited = set() # nodes with no cycles
        visiting = set()
        valid_ordering = []

        def has_cycles(node):

            if node in visited:
                return False
            if node in visiting:
                return True
            
            visiting.add(node)

            for neighbor in graph[node]:
                if has_cycles(neighbor):
                    return True

            visiting.remove(node)
            visited.add(node)
            # valid_ordering.insert(0, node) # this is O(n) since all elements need to be shifted
            valid_ordering.append(node)

        # 3. Apply it to all nodes (in case of disconnected graphs)
        for node in graph:
            # if node is already in visited, it'll return False right away
            if has_cycles(node):
                return []
        
        # Topological sort by appending at the start
        valid_ordering.reverse()
        return valid_ordering