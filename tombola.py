from random import choice, randint


def gen_cartella():
    C = []
    n = 1
    for i in range(9):
        C.append(randint(n, n + 9))
        n += 10
    while len(C) < 15:
        n = randint(1, 90)
        if n not in C and len([c for c in C if c // 10 == n // 10]) < 3:
            C.append(n)

    # slower but MUCH better generation
    T = [[] for i in range(3)]
    while not all([len(x) == 5 for x in T]):
        for n in C:
            i = randint(0, 2)
            if len(T[i]) == 5:
                continue
            if n // 10 not in [m // 10 for m in T[i]] and len(T[i]) < 5:
                T[i].append(n)

    [n.sort() for n in T]

    # R = [[] for i in range(3)]

    # while not all([len(x) == 5 for x in R]):
    #     i = 0
    #     for n in C:
    #         if len(R[i]) == 5:
    #             i += 1
    #         if i >= 3:
    #             break
    #         if n // 10 not in [m // 10 for m in R[i]] and len(R[i]) < 5:
    #             R[i].append(n)

    # [n.sort() for n in R]

    # shuffling
    # for m in range(5000):
    #     for i in range(len(R)):
    #         for j in range(1, len(R[0])):
    #             for k in range(10):
    #                 if R[i][j-1] // 10 == k and R[i][j] // 10 == k and randint(0, 1):
    #                     temp = R[i][j-1]
    #                     R[i][j-1] = R[i][j]
    #                     R[i][j] = temp

    # K = [n if n in [C for C in R] else None for n in range(1, 91)]

    # K = []
    # for i in range(len(R)):
    #     K.append([])
    #     for j in range(9):
    #         try:
    #             k = [n // 10 for n in R[i]].index(j)
    #             K[i].append(R[i][k])
    #         except ValueError:
    #             K[i].append(None)

    # shuffle a bit
    # print(K)
    # for i in range(1000):
    #     for j in range(len(K[0])):
    #         N = []
    #         for k in range(len(K)):
    #             if K[k][j] is not None and len(N) < 2:
    #                 N.append((k, j))
    #         if len(N) == 2 and randint(0, 1):
    #             temp = K[N[0][0]][N[0][1]]
    #             K[N[0][0]][N[0][1]] = K[N[1][0]][N[1][1]]
    #             K[N[1][0]][N[1][1]] = temp

    # K[0].append([n if i in [n // 10 for n in R[0]] else None])
    # K = [n if n in [sum(R[j] for j in range(3))] else None]
    # K = []
    # for c in C:

    # K = [[[n if n in c else None for n in range(
    #     i, i + 9)] for i in range(1, 91)] for c in C]
    # print(K)

    # return R

    return T


def vittoria(C, E, m):
    return any([len(set(E) & set(c)) >= m for c in C])


if __name__ == '__main__':
    # estrai 10 numeri a caso
    estratti = list(set([randint(1, 91) for i in range(10)]))
    # si va per l'ambo
    min_attuale = 2

    # genera cartella
    C = gen_cartella()
    # stampa se hai fatto ambo
    print(C, estratti, vittoria(C, estratti, min_attuale))
