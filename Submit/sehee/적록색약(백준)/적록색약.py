from collections import deque
import copy
N = int(input())
normal_picture = list(list(map(str, input())) for _ in range(N))
# notnormal_picture = copy.deepcopy(normal_picture)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


visited = [[0] * N for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and normal_picture[nx][ny] == normal_picture[x][y]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            count += 1
print(count, end=' ')


for i in range(N):
    for j in range(N):
        if normal_picture[i][j] == 'G':
            normal_picture[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            count += 1
print(count)







