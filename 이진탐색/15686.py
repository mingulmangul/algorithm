"""
[BOJ] 15686번: 치킨 배달
https://www.acmicpc.net/problem/15686

***
- 완전탐색
- m개의 치킨집을 뽑는 모든 조합에 대해 도시의 치킨 거리를 구함 -> 그 중 최솟값 출력
"""
from itertools import combinations

N, M = map(int, input().split())
chickens = []
houses = []
for i in range(N):
    for j, x in enumerate(input().split()):
        if x == "1":
            houses.append((i, j))
        elif x == "2":
            chickens.append((i, j))

min_chicken_dist = float('inf')
for comb in combinations(chickens, M):
    cur_chicken_dist = 0
    for r1, c1 in houses:
        min_dist = float('inf')
        for r2, c2 in comb:
            min_dist = min(min_dist, (abs(r1-r2) + abs(c1-c2)))
        cur_chicken_dist += min_dist
    min_chicken_dist = min(min_chicken_dist, cur_chicken_dist)
    
print(min_chicken_dist)