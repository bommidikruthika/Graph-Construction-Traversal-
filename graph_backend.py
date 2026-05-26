from collections import deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.graph = {}

    # Add Node
    def add_node(self, node):

        if node not in self.graph:
            self.graph[node] = []

    # Add Edge
    def add_edge(self, u, v, weight):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    # Display Graph
    def display(self):

        print("\nGraph:")

        if not self.graph:
            print("Graph is empty!")
            return

        for node in self.graph:

            print(f"{node} -> ", end="")

            for neighbor, weight in self.graph[node]:
                print(f"({neighbor}, {weight})", end=" ")

            print()

    # BFS Traversal
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        result = []

        while queue:

            node = queue.popleft()

            if node not in visited:

                result.append(node)
                visited.add(node)

                for neighbor, weight in self.graph[node]:

                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    # DFS Traversal
    def dfs(self, start):

        visited = set()
        result = []

        self.dfs_helper(start, visited, result)

        return result

    def dfs_helper(self, node, visited, result):

        visited.add(node)
        result.append(node)

        for neighbor, weight in self.graph[node]:

            if neighbor not in visited:
                self.dfs_helper(neighbor, visited, result)

    # Dijkstra Algorithm
    def dijkstra(self, start, end):

        distances = {}
        previous = {}

        for node in self.graph:
            distances[node] = float('inf')
            previous[node] = None

        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_node = heapq.heappop(priority_queue)

            for neighbor, weight in self.graph[current_node]:

                distance = current_distance + weight

                if distance < distances[neighbor]:

                    distances[neighbor] = distance
                    previous[neighbor] = current_node

                    heapq.heappush(
                        priority_queue,
                        (distance, neighbor)
                    )

        # Reconstruct Path
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path, distances[end]

    # Visualize Graph
    def visualize(self):

        G = nx.Graph()

        for node in self.graph:

            for neighbor, weight in self.graph[node]:

                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=2000,
            font_size=15
        )

        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labels
        )

        plt.show()