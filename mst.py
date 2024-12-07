import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def prim_mst(self):
        mst_cost = 0
        mst_edges = []
        visited = [False] * self.V
        min_heap = [(0, 0)]  # (weight, start_vertex)

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            mst_cost += weight
            mst_edges.append(u)

            for edge in self.graph[u]:
                if not visited[edge[1]]:
                    heapq.heappush(min_heap, edge)

        return mst_cost, mst_edges

# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
mst_cost, mst_edges = g.prim_mst()
print("MST Cost:", mst_cost)
print("MST Edges:", mst_edges)



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        self.edges.sort()
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        mst_cost = 0
        mst_edges = []

        for weight, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                mst_cost += weight
                mst_edges.append((u, v))
                self.union(parent, rank, x, y)

        return mst_cost, mst_edges

# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
mst_cost, mst_edges = g.kruskal_mst()
print("MST Cost:", mst_cost)
print("MST Edges:", mst_edges)