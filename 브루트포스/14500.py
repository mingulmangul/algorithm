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
"""
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def is_valid(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def solution1():
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0
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
    return answer

print(solution1())

