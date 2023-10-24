graph = [
    {2, 3},
    {1, 4, 5},
    {1, 6},
    {2},
    {2, 6},
    {3, 5}
]

visited = [False] * len(graph)


def depth_first_search(n):
    if visited[n - 1]:
        return
    visited[n - 1] = True
    print(n)
    for i in graph[n - 1]:
        depth_first_search(i)


depth_first_search(1)
