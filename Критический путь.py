graph = [
    {2, 3},
    {1, 4, 5},
    {1, 6},
    {2},
    {2},
    {3}
]


def depth_first_search(n):
    if visited[n - 1]:
        return []
    visited[n - 1] = True
    print(n)
    path = []
    for i in graph[n - 1]:
        cur_path = depth_first_search(i)
        if len(cur_path) > len(path):
            path = cur_path
    return [n] + path


visited = [False] * len(graph)
path = depth_first_search(1)
print(path)
visited = [False] * len(graph)
path = depth_first_search(path[-1])
print('Критический путь:', path, 'и его длина', len(path))