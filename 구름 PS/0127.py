import sys
from collections import deque
import heapq
def sol():
    q = []
    heapq.heappush(q, [1, 0, 0, 0])
    visit[0][0][0] = 1
    while q:
        # 데이터 존재할 때만 움직이는 반복문.
        # break 걸려있는것과 동일함
        cnt, x, y, c = heapq.heappop(q)
        if x == n - 1 and y == m - 1:
            return cnt

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][c] == 0:
                visit[nx][ny][c] = 1
                if matrix[nx][ny] == '0':
                    heapq.heappush(q, [cnt+1, nx, ny, c])
                if matrix[nx][ny] == '1' and c == 0:
                    heapq.heappush(q, [cnt + 1, nx, ny, 1])
    return -1

n, m = map(int, input().split())
matrix = list()
for i in range(n):
    matrix.append(input())
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
print(sol())