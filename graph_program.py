# Graph program


# Returns a label for each letter, like A1 and A2 when a letter repeats
def make_labels(name):
    labels = []
    seen = {}
    for letter in name:
        seen[letter] = seen.get(letter, 0) + 1
        if name.count(letter) > 1:
            labels.append(letter + str(seen[letter]))
        else:
            labels.append(letter)
    return labels


# A graph stored as an adjacency list
class Graph:
    # Creates a graph with one vertex per label and no edges
    def __init__(self, labels):
        self.labels = labels
        self.adjacency = {}
        for i in range(len(labels)):
            self.adjacency[i] = []

    # Connects two vertices with an edge
    def add_edge(self, a, b):
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)
        self.adjacency[a].sort()
        self.adjacency[b].sort()

    # BFS: visits the vertices level by level using a queue
    def bfs(self, start):
        order = []
        visited = [False] * len(self.labels)
        queue = [start]
        visited[start] = True
        while queue:
            current = queue.pop(0)
            order.append(self.labels[current])
            for neighbor in self.adjacency[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order

    # DFS: goes as deep as possible, then goes back (recursion)
    def dfs(self, vertex, visited, order):
        visited[vertex] = True
        order.append(self.labels[vertex])
        for neighbor in self.adjacency[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, order)

    # Shows every vertex with its neighbors
    def display(self):
        for i in range(len(self.labels)):
            neighbors = []
            for n in self.adjacency[i]:
                neighbors.append(self.labels[n])
            print(self.labels[i], ":", ", ".join(neighbors))


# Builds the edges of the graph from the number of letters
def build_graph(labels):
    graph = Graph(labels)
    n = len(labels)

    # Connect each letter to its two children (like the tree)
    for i in range(n):
        for child in (2 * i + 1, 2 * i + 2):
            if child < n:
                graph.add_edge(i, child)

    # Extra edges that make cycles (G-U and U-E for OANAGUEN)
    for i in range(n // 2, n - 2):
        graph.add_edge(i, i + 1)

    return graph


# Builds a graph from the name, then shows BFS and DFS
def run():
    name = input("Enter your last name: ").upper()
    if name == "":
        print("Name cannot be empty.")
        return

    graph = build_graph(make_labels(name))

    print("\n--- Graph (adjacency list) ---")
    graph.display()

    # BFS starting at the first letter
    print("\n--- BFS ---")
    print(" ".join(graph.bfs(0)))

    # DFS starting at the first letter
    print("\n--- DFS ---")
    order = []
    graph.dfs(0, [False] * len(graph.labels), order)
    print(" ".join(order))


if __name__ == "__main__":
    run()
