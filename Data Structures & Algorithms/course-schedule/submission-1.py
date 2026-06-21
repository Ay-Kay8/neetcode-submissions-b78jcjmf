class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # node: [connectedTo, ...]
        graph = dict([(i, []) for i in range(numCourses)])
        for connectedTo, node in prerequisites:
            graph[node].append(connectedTo) 

        visited = set() # contains nodes with no cycles
        visiting = set() # contains nodes in current path
        def has_cycles(node):
            if node in visited:
                return False
            if node in visiting:
                return True # cycle detected
            
            visiting.add(node)
            
            # recur over all neighbors
            for neighbor in graph.get(node, []):
                if has_cycles(neighbor):
                    return True
                
            # we're done exploring this node, move it from visiting to visited
            visiting.remove(node)
            visited.add(node)

            return False
                
        for node in graph:
            if node not in visited:
                if has_cycles(node):
                    return False
        
        return True

