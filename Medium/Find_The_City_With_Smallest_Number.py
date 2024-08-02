class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # dfs or bfs? probably bfs. Within bfs there are many algorithms and one is djikstras
        # this is helpful because we have a threshold and will find the shortest path
        # run this algorithm on every node
        adjList = defaultdict(list) # put list in here so default value is the default value of a list

        # fill our dictionary up with all immediate neighbors
        for v1, v2, dist in edges:
            adjList[v1].append((v2, dist))
            adjList[v2].append((v1, dist))

        def dijkstra(src):
            heap = [(0, src)] # dist, node
            can_visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in can_visit:
                    continue
                can_visit.add(node)
                for neighbor, dist2 in adjList[node]:
                    neighbor_distance = dist + dist2
                    if neighbor_distance <= distanceThreshold:
                        heapq.heappush(heap, (neighbor_distance, neighbor))

            return len(can_visit) - 1
        
        res, min_nodes_reached = -1, float("inf")
        for src in range(n):
            nodes_reached = dijkstra(src)
            if nodes_reached <= min_nodes_reached:
                res, min_nodes_reached = src, nodes_reached

        return res