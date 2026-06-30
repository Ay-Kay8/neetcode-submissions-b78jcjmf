class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # each node is its own parent to start
        parents = [i for i in range(len(edges) + 1)] # ith node -> parent ([1, n])

        rank = [1] * (len(edges) + 1)

        def find(n):
            """
            Find the parent of n
            """
            # if n is its own parent, then just return it
            if n == parents[n]:
                return parents[n]
            
            # else find the parent of its parent
            # and then set it
            parents[n] = find(parents[n])
            return parents[n]

        def union(n1, n2):
            """
            Returns True if n1 and n2 are not connected
            """
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                # they are connected
                return False
            
            # idk what rank is
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            # for every edge, if n1 - n2 cause a cycle, then
            # removing it will NOT disconnected the graph
            # and WILL eliminate the cycle
            if not union(n1, n2):
                return [n1, n2]
