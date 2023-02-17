"""
2580번: 스도쿠
https://www.acmicpc.net/problem/2580

***
참고:
https://hongcoding.tistory.com/118
https://suri78.tistory.com/76
"""
import sys
input = sys.stdin.readline

# 입력
puzzle = [list(map(int, input().split())) for _ in range(9)]
# 빈 칸(0)의 좌표
zero = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]

# 스도쿠 판 출력
def print_puzzle():
    for row in puzzle:
        print(" ".join(map(str, row)))
        
# num이 puzzle[r][c]에 들어갈 수 있는지 확인
def is_valid(num, r, c):
    # 같은 행,열에 num과 같은 숫자가 있다면, False 리턴
    for i in range(9):
        if puzzle[i][c] == num or puzzle[r][i] == num:
            return False
    # 같은 칸에 같은 숫자 있다면, False 리턴
    for i in range((r // 3) * 3, ((r // 3) * 3) + 3):
        for j in range((c // 3) * 3, ((c // 3) * 3) + 3):
            if puzzle[i][j] == num:
                return False
    return True

# DFS
def sudoku(idx):
    # 빈 칸을 모두 채웠다면, 스도쿠 판 출력 후 종료
    if idx == len(zero):
        print_puzzle()
        sys.exit(0)
    # idx번째 빈 칸
    r, c = zero[idx]
    for num in range(1, 10):
        # num(1~9)이 해당 빈 칸에 들어갈 수 있다면
        if is_valid(num, r, c):
            puzzle[r][c] = num  # 빈 칸에 num을 넣고
            sudoku(idx + 1)     # 다음 빈 칸에 대한 탐색 시작
            puzzle[r][c] = 0    # num이 정답이 아닐 수 있으므로 0으로 다시 돌림
    
sudoku(0)