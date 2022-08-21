import sys

test_n = int(sys.stdin.readline())

for _ in range(test_n):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    graph = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        graph[0][i] = i
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            temp = 0
            for u in range(j):
                temp += graph[i - 1][u + 1]
            graph[i][j] = temp
    
    print(graph[k][n])