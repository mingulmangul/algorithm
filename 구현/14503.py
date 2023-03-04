"""
14503번 로봇 청소기: https://www.acmicpc.net/problem/14503
- 구현
"""
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 방향: 북, 동, 남, 서
    
def clean(room, r, c, d, ans):
    # 현재 칸 청소
    if room[r][c] == 0:
        ans += 1
        room[r][c] = -1
    # 청소되지 않은 빈 칸으로 이동
    nd = d
    for i in range(4):
        nd = (nd + 3) % 4
        dr, dc = direction[nd]
        nr, nc = r + dr, c + dc
        if 0 < nr < N-1 and 0 < nc < M-1 and room[nr][nc] == 0:
            ans = clean(room, nr, nc, nd, ans)
            break
    # 청소할 칸이 없다면 후진
    else:
        dr, dc = direction[(d + 2) % 4]
        nr, nc = r + dr, c + dc
        if 0 < nr < N-1 and 0 < nc < M-1 and room[nr][nc] < 1:
            ans = clean(room, nr, nc, d, ans)
    return ans

print(clean(room, r, c, d, 0))