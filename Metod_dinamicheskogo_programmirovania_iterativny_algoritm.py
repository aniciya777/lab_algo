from math import factorial
from itertools import combinations

M = [
    [None, 15, 2, 9, 2],
    [9, None, 3, 9, 3],
    [2, 13, None, 12, 3],
    [6, 2, 14, None, 12],
    [3, 17, 6, 8, None]
]

def print_matrix(M):
    size = len(M)
    print(' ' * 5 + '\t' + '\t'.join(f'c{i + 1}' for i in range(size)))
    print(' ' * 4 + '┌' + '\t' * (size + 1) + '┐')
    for row in range(size):
        if row == (size) // 2:
            print('B = │', end='')
        else:
            print('    │', end='')
        print('\t' + '\t'.join(str(x) if (x is not None) else '' for x in M[row]) + f'\t│\tc{row + 1}')
    print(' ' * 4 + '└' + '\t' * (size + 1) + '┘')


def print_set(st):
    ls = list(st)
    if len(ls) == 0:
        return '∅'
    if len(ls) == 1:
        return f'c{ls[0]}'
    return '{c' + ',c'.join(map(str, ls)) + '}'


def count_combinations(k, n):
    return factorial(n) // (factorial(k) * factorial(n - k))


def rjust_strings(strings):
    '''
    Выравнивание строк по ширине
    '''
    max_width = max(map(len, strings))
    for i in range(len(strings)):
        strings[i] += ' ' * (max_width - len(strings[i]))
    return strings


def dinamic_traveler(M, start=1):
    size = len(M)
    memory = dict()
    print(f'Решение задачи для {size} городов c{",c".join(map(str, range(1, 1 + size)))} с матрицей расстояний')
    print_matrix(M)
    print(
        f'''За начало маршрута примем город c{start}. Тогда
    (c{start}, C{size - 1}) = f(c{start}, {print_set(i for i in range(1, 1 + size) if i != start)})
представляет собой длину кратчайшего маршрута, и любая очередность
посещения городов, приводящая к этой длине маршрута, является оптимальной.''')
    for k in range(size - 1):
        count_variables = (size - 1) * count_combinations(k, size - 2)
        print(f'Шаг {k} (k={k}), {count_variables} вариант(a/ов)', end='')
        if k:
            print(f'; решения при k={k} выражаются через известные решения при k={k - 1}', end='')
        print(':')
        for i in range(1, 1 + size):
            if i != start:
                if k == 0:
                    value = M[i - 1][start - 1]
                    memory[(i, frozenset())] = (value, None)
                    print(f'    f(c{i}, ∅) = b{i}{start}={value}')
                else:
                    C_other = [i for i in range(1, 1 + size)]
                    C_other.remove(i)
                    C_other.remove(start)
                    for comb in combinations(C_other, k):
                        if k == 1:
                            summands = [M[i - 1][comb[0] - 1], memory[(comb[0], frozenset())][0]]
                            value = sum(summands)
                            memory[(i, frozenset({comb[0]}))] = (value, comb[0])
                            print(
                                f'    f(c{i}, c{comb[0]}) = b{i}{comb[0]} + f(c{comb[0]}, ∅) = b{i}{comb[0]} + b{comb[0]}{start} = {" + ".join(map(str, summands))} = {value}')
                        else:
                            expressions1 = []
                            expressions2 = []
                            values = []
                            for x in comb:
                                comb2 = list(comb)
                                comb2.remove(x)
                                sl1 = M[i - 1][x - 1]
                                sl2 = memory[(x, frozenset(comb2))][0]
                                expressions1.append(f'b{i}{x} + f(c{x}, {print_set(comb2)})')
                                expressions2.append(f'{sl1} + {sl2}')
                                values.append(sl1 + sl2)
                            value = min(values)
                            n = len(values)
                            memory[(i, frozenset(comb))] = (value, comb[values.index(value)])
                            strings = [f'    f(c{i}, {print_set(comb)}) = min ┌']
                            for j in range(1, n - 1):
                                strings.append(' ' * (len(strings[0]) - 1) + '│')
                            strings.append(' ' * (len(strings[0]) - 1) + '└')
                            for j in range(n):
                                if values[j] == value:
                                    strings[j] += f' -->{expressions1[j]}<-- '
                                else:
                                    strings[j] += f'    {expressions1[j]}    '
                            strings = rjust_strings(strings)
                            strings[0] += '┐ = min ┌'
                            for j in range(1, n - 1):
                                strings[j] += '│       │'
                            strings[-1] += '┘       └'
                            for j in range(n):
                                if values[j] == value:
                                    strings[j] += f' -->{expressions2[j]}<-- '
                                else:
                                    strings[j] += f'    {expressions2[j]}    '
                            strings = rjust_strings(strings)
                            strings[0] += f'┐ = {value}'
                            for j in range(1, n - 1):
                                strings[j] += '│'
                            strings[-1] += '┘'
                            for s in strings:
                                print(s)
        if (k == 2):
            print(
                '''На втором шаге (и следующих шагах) осуществляется выбор – определяется минимум.
Выбранный член должен быть зафиксирован, так как он соответствует фактическому
направлению движения. Зафиксированные члены выделены --> <--.''')
    k = size - 1
    print(f'Шаг {k} (k={k}), 1 вариант; решения при 𝑘={k} выражаются через известные решения при 𝑘={k - 1}:')

    C_other = [i for i in range(1, 1 + size)]
    C_other.remove(start)
    for comb in combinations(C_other, k):
        expressions1 = []
        expressions2 = []
        values = []
        for x in comb:
            comb2 = list(comb)
            comb2.remove(x)
            sl1 = M[start - 1][x - 1]
            sl2 = memory[(x, frozenset(comb2))][0]
            expressions1.append(f'b{start}{x} + f(c{x}, {print_set(comb2)})')
            expressions2.append(f'{sl1} + {sl2}')
            values.append(sl1 + sl2)
        value = min(values)
        n = len(values)
        memory[(start, frozenset(comb))] = (value, comb[values.index(value)])
        strings = [f'    f(c{start}, {print_set(comb)}) = min ┌']
        for j in range(1, n - 1):
            strings.append(' ' * (len(strings[0]) - 1) + '│')
        strings.append(' ' * (len(strings[0]) - 1) + '└')
        for j in range(n):
            if values[j] == value:
                strings[j] += f' -->{expressions1[j]}<-- '
            else:
                strings[j] += f'    {expressions1[j]}    '
        strings = rjust_strings(strings)
        strings[0] += '┐ = min ┌'
        for j in range(1, n - 1):
            strings[j] += '│       │'
        strings[-1] += '┘       └'
        for j in range(n):
            if values[j] == value:
                strings[j] += f' -->{expressions2[j]}<-- '
            else:
                strings[j] += f'    {expressions2[j]}    '
        strings = rjust_strings(strings)
        strings[0] += f'┐ = {value}'
        for j in range(1, n - 1):
            strings[j] += '│'
        strings[-1] += '┘'
        for s in strings:
            print(s)
    print(f'Таким образом, кратчайший маршрут имеет длину {value}. Восстановим его, пройдя шаги в обратном порядке: {", ".join(map(str, range(size - 1, -1, -1)))}.')
    path = [start]
    strings = []
    index = start
    for step in range(size - 1, 0, -1):
        next_value, next_index = memory[(index, frozenset(C_other))]
        path.append(next_index)
        next_C_other = C_other.copy()
        next_C_other.remove(next_index)
        sl1 = M[index - 1][next_index - 1]
        sl2 = next_value - sl1
        strings.append(f'    Шаг {step}:    {next_value} = f(c{index}, {print_set(C_other)}) = b{index}{next_index} + f(c{next_index}, {print_set(next_C_other)}) = {sl1} + {sl2},')
        index = next_index
        C_other = next_C_other
    strings.append(f'    Шаг 0:    {sl2} = f(c{path[-1]}, ∅) = b{path[-1]}{start} = {sl2},')
    strings = rjust_strings(strings)
    path.append(start)
    for i, s in enumerate(strings):
        s += f'    c{path[i]} → c{path[i + 1]}.'
        print(s)
    print('Кратчайший маршрут имеет вид')
    print('    ' + ' → '.join(map(str, path)))
    return value, path


print('МЕТОД ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ')
dist, path = dinamic_traveler(M, start=1)
