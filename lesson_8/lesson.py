# последовательный просмотр отдельных уровней графа, начиная с узла источника
# берем первую вершину и помещаем в пустую очередь.
# далее цикл. извлекаем из очереди вершину. если вершина целевая, то конец поиска.
# тначе в конец очереди добавляются все смежные вершины, которые еще не пройдены и не находятся
# в очереди.
# далее следующий виток цикла. если очередь пуста, то все вершины графа просмотрены и целевой узел не достижим


from collections import deque

gr = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
print(*gr, sep='\n')


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]  # родитель для каждой вершины
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True  # посетили 1 вершину, не будем заходить в нее в цикле

    while len(deq) > 0:
        curent = deq.pop()  # извлекаем вершину, отправная точка
        if curent == finish:
            # return parent
            break
        # смотри мвсе вершины, связанные с текущей
        for i, vertex in enumerate(graph[curent]):  # строка curent из графа
            if vertex == 1 and not is_visited[i]:  # ЕСЛИ 1, значит можем перейти в вершину из текущей и не посещали еще
                is_visited[i] = True
                parent[i] = curent  # указываем в списке откуда пришли
                deq.appendleft(i)

    else:
        return f'из {start} не попасть в {finish}'

    cost = 0
    way = deque([finish])  # добавим в очередь цель
    i = finish  # потребуется, чтобы пройтись по вершщинам от конца к началу

    while parent[i] != start:  # пока не доши до первой вершины
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'путь {list(way)} длинной {cost}'


s = 1
f = 3
print(bfs(gr, s, f))
