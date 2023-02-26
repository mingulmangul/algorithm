"""
2638번: 치즈
https://www.acmicpc.net/problem/2638

BFS
- 치즈 칸 탐색 시 1씩 증가(외부랑 닿는 면 개수)
- 3 이상인 치즈 녹임 -> 0으로 바꿈
- 모든 치즈를 녹일 때까지 반복

***
참고: https://resilient-923.tistory.com/318
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
while True:    
    # 치즈가 외부 공기와 닿는 면 개수 계산하기
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] > 0:
                    arr[nr][nc] += 1
                elif not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    # 외부와 2면 이상 닿는 치즈 녹이기
    flag = False
    for r in range(N):
        for c in range(M):
            if arr[r][c] >= 3:
                flag = True
                arr[r][c] = 0
            elif arr[r][c] == 2:
                arr[r][c] = 1
    # 더이상 녹일 치즈가 없으면 반복 종료
    if flag:
        cnt += 1
    else:
        break

print(cnt)