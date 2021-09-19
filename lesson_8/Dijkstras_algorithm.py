# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

gr = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length  # стоимость пути до вершины. изначально бесконечность
    parent = [-1] * length  # потом -1 поменяем на родителя

    cost[start] = 0
    min_cost = 0  # будет показывать движемся по графу или уже нет

    while min_cost < float('inf'):
        is_visited[start] = True  # в данный момент стартовая вершина, потом поменяем на другую

        for i, vertex in enumerate(graph[start]):  # гоняем по строке графа соответсвующей стартовой вершине
            if vertex != 0 and not is_visited[i]:  # значение вершины != 0, значит есть ребро и вершину не посещали
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):  # цикл по всем вершинам графа
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    ways = []
    for i in range(length):
        j = i
        way = [i]
        while parent[j] != -1:
            way.append(parent[j])
            j = parent[j]
        ways.append(way)
    return cost, ways

    return cost, ways


s = 0
print(dijkstra(gr, s))
