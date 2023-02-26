"""
14500번: 테트로미노
https://www.acmicpc.net/problem/14500

- 완전 탐색 + 최대힙을 이용한 BFS(합이 가장 큰 테트로미노 만들기)
  → 실패
- 반례 (solution1)
5 5
0 0 0 0 0
100 0 0 2 0 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
답: 102 / 출력: 100

- BFS 대신 DFS 이용
***
참고: https://heytech.tistory.com/364
"""
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def is_valid(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

# BFS -> 실패
def solution1():
    global answer
    # 완전탐색
    for i in range(N):
        for j in range(M):
            tetro = []  # 테트로미노로 선택된 칸
            result = 0  # 테트로미노가 놓인 칸의 합
            h = [(-arr[i][j], i, j)]  # 최대힙
            
            while h:
                element = heapq.heappop(h)  # 가장 큰 수인 칸
                
                # 테트로미노로 선택
                tetro.append(element)
                result -= element[0]
                # 테트로미노 완성 시 반복 종료
                if len(tetro) == 4:
                    break
                
                # 현재 칸의 상하좌우를 힙에 추가
                for di, dj in d:
                    next_i = element[1] + di
                    next_j = element[2] + dj
                    if is_valid(next_i, next_j):
                        next_element = (-arr[next_i][next_j], next_i, next_j)
                        if next_element not in tetro:
                            heapq.heappush(h, next_element)
                
            # 최댓값 갱신
            answer = max(answer, result)
            
### DFS 이용 -> 파이썬은 시간초과, PyPy3로 통과 (1256ms)
### dfs에 종료 조건을 추가 (파이썬으로 180ms)
visited = [[False] * M for _ in range(N)]
max_value = max(map(max, arr))

def dfs(i, j, cnt, result):
    global answer
    # 추가한 종료 조건: 블록을 더 붙여도 최댓값을 갱신할 수 없는 경우
    if result + max_value * (4 - cnt) <= answer:
        return
    
    if cnt == 4:
        answer = max(answer, result)
        return
    
    for di, dj in d:
        next_i = i + di
        next_j = j + dj
        if is_valid(next_i, next_j) and not visited[next_i][next_j]:
            if cnt == 2:
                visited[next_i][next_j] = True
                dfs(i, j, cnt + 1, result + arr[next_i][next_j])
                visited[next_i][next_j] = False
            visited[next_i][next_j] = True
            dfs(next_i, next_j, cnt + 1, result + arr[next_i][next_j])
            visited[next_i][next_j] = False
    
def solution2():
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, arr[i][j])
            visited[i][j] = False
    return answer

print(solution2())