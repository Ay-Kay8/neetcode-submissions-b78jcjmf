class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. make graph
        graph = dict([(i, []) for i in range(numCourses)])

        for destination, source in prerequisites:
            graph[source].append(destination)

        # 2. dfs
        visited = set() # nodes without cycles
        visiting = set() # nodes on the current path

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

        # 3. dfs on all nodes
        for node in graph:
            if has_cycles(node):
                return False
        
        return True