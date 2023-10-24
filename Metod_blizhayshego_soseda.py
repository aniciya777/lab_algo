M = [
    [None, 15, 2, 9, 2],
    [9, None, 3, 9, 3],
    [2, 13, None, 12, 3],
    [6, 2, 14, None, 12],
    [3, 17, 6, 8, None]
]


def nearest_neighbor_traveler(M, start):
    size = len(M)
    dist = 0
    path = [start]
    C_other = set(range(1, size + 1)) - {start}
    while C_other:
        C_i_optim = None
        dist_i_opt = None
        for C_i in C_other:
            dist_i = M[path[-1] - 1][C_i - 1]
            if dist_i_opt is None or dist_i < dist_i_opt:
                C_i_optim = C_i
                dist_i_opt = dist_i
        dist += dist_i_opt
        path.append(C_i_optim)
        C_other.discard(C_i_optim)
    dist += M[path[-1] - 1][start - 1]
    path.append(start)
    return dist, path


dist, path = nearest_neighbor_traveler(M, start=2)
print('МЕТОД БЛИЖАЙШЕГО СОСЕДА')
print('Кратчайший машртрут имеет вид: ', ' -> '.join(map(str, path)))
print('Его длина равна', dist)
print()

dist, path = nearest_neighbor_traveler(M, start=1)
print('МЕТОД БЛИЖАЙШЕГО СОСЕДА')
print('Кратчайший машртрут имеет вид: ', ' -> '.join(map(str, path)))
print('Его длина равна', dist)
print('### НЕОПТМИМАЛЬНОЕ РЕШЕНИЕ! ###')
print()
