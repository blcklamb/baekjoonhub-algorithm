# https://www.acmicpc.net/problem/10971

N = int(input())
W = []

for _ in range(N):
    row = list(map(int, input().split()))
    W.append(row)

minByStartCity = [float('inf') for _ in range(N)]


def circuitByStartCity(current, visited, answer):
    global W, minAnswer, start

    if visited.count(True) == N:
        if W[current][start] != 0:
            minAnswer = min(minAnswer, answer+W[current][start])
        return

    for i in range(N):

        if visited[i] or i == current:
            continue
        if W[current][i] == 0:
            continue

        visited[i] = True
        answer += W[current][i]
        circuitByStartCity(i, visited, answer)
        visited[i] = False
        answer -= W[current][i]


for i in range(N):
    minAnswer = float('inf')
    visited = [False if j != i else True for j in range(N)]
    start = i
    circuitByStartCity(i, visited, 0)
    minByStartCity[i] = minAnswer


print(min(minByStartCity))
