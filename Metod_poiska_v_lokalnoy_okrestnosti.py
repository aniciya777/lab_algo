M = [
    [None, 15, 2, 9, 2],
    [9, None, 3, 9, 3],
    [2, 13, None, 12, 3],
    [6, 2, 14, None, 12],
    [3, 17, 6, 8, None]
]


def search_in_local_area(M, base_path=None):
    def get_dist(path):
        return sum(M[path[i] - 1][path[(i + 1) % size] - 1] for i in range(len(path)))

    size = len(M)
    if base_path is None:
        base_path = list(range(1, size + 1))
    path_opt = base_path
    print('1.      Выберем опорный маршрут:')
    print('        π = (', ', '.join(map(str, path_opt)), ')', sep='', end=', ')
    dist_opt = get_dist(path_opt)
    print(f'Lmin = {dist_opt}.')
    punkt = 0
    while True:
        print(f'''{punkt * 2 + 2}.      В 1-окрестности N1(π{punkt if punkt else ''}) будем искать маршрут π{punkt + 1},
        удовлетворяющие условию L < Lmin, где L — длина пути.''')
        path_opt_local = None
        for i in range(size):
            for j in range(size):
                if i != j:
                    path_new = path_opt.copy()
                    element = path_new.pop(i)
                    path_new.insert(j, element)
                    dist = get_dist(path_new)
                    if dist < dist_opt:
                        dist_opt = dist
                        path_opt_local = (path_new, i, j)
                    print(
                        f'        Ω{i + 1},{j + 1}(π{punkt if punkt else ""}) = ({", ".join(map(str, path_new))}), L = {dist}')
            print()
        if path_opt_local is None:
            break
        path_opt = path_opt_local[0]
        print(f'''{punkt * 2 + 3}.      В результате получили, что:
        π{punkt + 1} = Ω{path_opt_local[1] + 1},{path_opt_local[2] + 1}(π{punkt if punkt else ''}) = ({", ".join(map(str, path_opt_local[0]))}), L = {dist_opt} — искомое 1-оптимальное решение.
        π{punkt + 1} = ({", ".join(map(str, path_opt_local[0]))})
        Пусть Lmin = {dist_opt}.''')
        punkt += 1
    print(f'''{punkt * 2 + 3}.      Решение (маршрут) ({", ".join(map(str, path_opt))}) = π{punkt}, L = {dist_opt} является лучшим в своей 1-окрестности.
        Это 1-оптимальное решение.''')
    return dist_opt, path_opt + path_opt[:1]


print('МЕТОД ПОИСКА В ЛОКАЛЬНОЙ ОКРЕСТНОСТИ')
print('(приближенное 1-оптимальное решение)')
print()
dist, path = search_in_local_area(M)
