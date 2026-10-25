
def dls(graph, node, goal, limit, path):
    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(
                graph, neighbor, goal,
                limit - 1, path + [neighbor]
            )

            if result is not None:
                return result

    return None


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth, [start])

        if result is not None:
            print("Path found:", result)
            print("Depth:", len(result) - 1)
            return

    print("No path found")


# Main program
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    neighbors = input(
        f"Enter neighbors of {node} separated by spaces: "
    ).split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

iddfs(graph, start, goal, max_depth)
