M = [
    [None, 15, 6, 19, 9, 14],
    [16, None, 3, 19, 13, 12],
    [22, 23, None, 22, 23, 9],
    [16, 9, 4, None, 21, 11],
    [13, 17, 5, 17, None, 35],
    [4, 2, 2, 4, 3, None]
]


def dinamic_traveler(M, start=1):
    def dinamic_traveler_recursive(M, start, C_i, C_k):
        if not C_k:
            '''
                Возвращаем 2 значения
                - наикратчайшее расстояние
                - кортеж из маршрута
            '''
            return M[C_i - 1][start - 1], (C_i, start)
        dist_opt = None
        path_opt = None
        for C_j in C_k:
            dist, path = dinamic_traveler_recursive(M, start, C_j, C_k - {C_j})
            dist += M[C_i - 1][C_j - 1]
            if dist_opt is None or dist < dist_opt:
                dist_opt = dist
                path_opt = path
        return dist_opt, (C_i,) + path_opt

    size = len(M)
    C_k = set(range(1, size + 1)) - {start}
    return dinamic_traveler_recursive(M, start, start, C_k)


dist, path = dinamic_traveler(M)
print('МЕТОД ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ')
print('Кратчайший машртрут имеет вид: ', ' -> '.join(map(str, path)))
print('Его длина равна', dist)
print()
