from itertools import combinations, permutations
from collections import deque
import copy

N, M = map(int, input().split())

laboratory = list(list(map(int,input().split())) for _ in range(N))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]



def bfs(q):
    while q:
        global qu

        a, b = q.popleft()
        visited[a][b] = 1

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and qu[nx][ny] == 0:
                visited[nx][ny] = 1
                qu[nx][ny] = 2
                q.append([nx, ny])


cand = []
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            cand.append([i,j])

combi = list(combinations(cand, 3))

answer = 0
for cd in combi:
    visited = [[0] * M for _ in range(N)]
    qu = copy.deepcopy(laboratory) # 복사하는 거 생각 못해서 시간 엄청 오래 걸림

    for x, y in cd:
        qu[x][y] = 1

    que = deque()
    for i in range(N):
        for j in range(M):
            if qu[i][j] == 2:
                que.append([i, j])
    bfs(que)

    cnt = 0
    for i in range(N):
        cnt += qu[i].count(0)

    answer = max(cnt, answer)
print(answer)

