"""
9663번 N-Queen: https://www.acmicpc.net/problem/9663

백트래킹
"""
## 시간 초과
N = int(input())
is_queen = [[False] * N for _ in range(N)]
answer = 0

# (i, j)에 퀸을 놓을 수 있는지 판별
def can_set_queen(i, j):
    for k in range(i):
        if is_queen[k][j] or (abs(i - k) == abs(j - is_queen[k].index(True))):
            return False
    return True

# 백트래킹
def backtracking(cnt):
    global answer
    # N개의 퀸을 다 놓았으면 경우의 수 카운트
    if cnt >= N:
        answer += 1
        return
    # cnt행에 퀸을 놓을 수 있다면 백트래킹 이어감
    for j in range(N):
        if can_set_queen(cnt, j):
            is_queen[cnt][j] = True
            backtracking(cnt+1)
            is_queen[cnt][j] = False
                
backtracking(0)
print(answer)