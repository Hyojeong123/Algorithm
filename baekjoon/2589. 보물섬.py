from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def bfs(x, y):
    dist = 0
    q = deque()
    q.append((x, y, dist))
    visited[x][y] = 1
    while q:
        r, c, d = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and treasure_map[nr][nc] == 'L' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc, d+1))
                dist = d + 1
                
    return dist


R, C = map(int, input().split())
treasure_map = [input() for _ in range(R)]
max_dist = 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 육지를 만나면 bfs를 돌려서 가장 먼 최단거리를 찾는다
# max_dist와 비교하며 최댓값을 갱신한다
for i in range(R):
    for j in range(C):
        if treasure_map[i][j] == 'L':
            visited = [[0] * C for _ in range(R)]
            max_dist = max(max_dist, bfs(i, j))

print(max_dist)
