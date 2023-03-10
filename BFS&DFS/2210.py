"""
2210번 숫자판 점프: https://www.acmicpc.net/problem/2210

브루트포스
"""
board = [list(input().split()) for _ in range(5)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
ans_set = set()

def dfs(i, j, num):
    if len(num) == 6:
        ans_set.add(num)
        return
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, num + board[ni][nj])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])
                    
print(len(ans_set))