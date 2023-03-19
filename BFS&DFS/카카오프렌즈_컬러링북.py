"""
카카오프렌즈 컬러링북: https://school.programmers.co.kr/learn/courses/30/lessons/1829
- BFS
  - 0이면 패스
  - 0이 아니면 BFS 시작 (방문 체크 + 영역 개수 & 크기 카운팅)
- 출력: [영역 개수, 가장 큰 영역 크기]
"""
from collections import deque

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(m, n, picture):
    size_of_area = dict()   # {영역: 영역 넓이}
    for i in range(m):
        for j in range(n):
            # 색칠하지 않는 경우 패스
            if picture[i][j] == 0:
                size_of_area[0] = 0  # 0 영역도 개수에 포함하기 위해 딕셔너리에 추가
                continue
            # 이미 탐색한 경우 패스
            if picture[i][j] < 0:
                continue
            # 초기화
            color = picture[i][j]
            cur_size = 0
            q = deque()
            q.append((i, j))
            picture[i][j] = -1
            # BFS
            while q:
                i, j = q.popleft()
                cur_size += 1
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and picture[ni][nj] == color:
                        q.append((ni, nj))
                        picture[ni][nj] = -1
            # 영역 넓이 갱신
            size_of_area[color] = max(size_of_area.get(color, 0), cur_size)
            print(size_of_area)
    
    return [len(size_of_area), max(size_of_area.values())]

# 테스트 입력
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
print(solution(len(picture), len(picture[0]), picture))