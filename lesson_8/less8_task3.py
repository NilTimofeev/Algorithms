num = 5


def create_graph(n):
    graph = {j: {i for i in range(n) if i != j} for j in range(n)}
    return graph


def dfs(graph, vertex, visited):
    # if vertex not in visited:
    visited.append(vertex)
    for k in graph[vertex]:
        if k not in visited:
            dfs(graph, k, visited)
    return visited


print(dfs(create_graph(num), 0, []))

