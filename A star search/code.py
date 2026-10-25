
import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]

    g = {start: 0}
    parent = {start: None}
    visited = {}

    while pq:
        f, cost, node = heapq.heappop(pq)

        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        if node == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Path found:", path)
            print("Total cost:", cost)
            return

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost

            if new_cost < g.get(neighbor, float("inf")):
                g[neighbor] = new_cost
                parent[neighbor] = node
                new_f = new_cost + heuristic[neighbor]

                heapq.heappush(
                    pq, (new_f, new_cost, neighbor)
                )

    print("No path found")


# Main program
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    heuristic[node] = int(
        input(f"Enter heuristic value of {node}: ")
    )

    graph[node] = []

m = int(input("Enter number of edges: "))

for i in range(m):
    u, v, cost = input(
        "Enter edge (node1 node2 cost): "
    ).split()

    cost = int(cost)

    graph[u].append((v, cost))
    graph[v].append((u, cost))  # Undirected graph

start = input("Enter start node: ")
goal = input("Enter goal node: ")

astar(graph, heuristic, start, goal)
