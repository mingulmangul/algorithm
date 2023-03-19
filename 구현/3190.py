"""
3190번 뱀: https://www.acmicpc.net/problem/3190
- 구현
"""
from collections import deque
import sys
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
K = int(input().rstrip())
apples = {tuple(map(int, input().split())) for _ in range(K)}
L = int(input().rstrip())
changes = deque([list(input().split()) for _ in range(L)])

# 방향
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

snake = deque([(1, 1)])  # 뱀의 몸 (첫 번째 원소: 머리 / 마지막 원소: 꼬리)
answer = 0               # 게임 시작 후 지난 시간

while True:
    # 방향 전환할 때가 되었다면
    if changes and answer == int(changes[0][0]):
        X, C = changes.popleft()
        d = 3 if C == 'L' else 1    # L이면 왼쪽, D면 오른쪽으로 회전
        direction = (direction + d) % 4
    # 현재 방향으로 이동
    hi, hj = snake[0]
    ni = hi + move[direction][0]
    nj = hj + move[direction][1]
    next_node = (ni, nj)
    # 시간 카운트
    answer += 1
    # 벽 또는 몸에 부딪히는 경우 종료
    if not (0 < ni <= N and 0 < nj <= N) or next_node in snake:
        print(answer)
        break
    # 이동 가능하면 이동
    snake.appendleft(next_node)
    if next_node in apples:       # 사과가 있는 칸으로 이동한 경우
        apples.remove(next_node)  # 사과 제거
    else:                         # 빈 칸으로 이동한 경우
        snake.pop()               # 꼬리 이동
        