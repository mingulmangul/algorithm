"""
합승 택시 요금: https://school.programmers.co.kr/learn/courses/30/lessons/72413
- 최단 경로 찾기
  1. 합승 비용 계산
    모든 n에 대해 n지점까지 가는 비용 계산
  2. 개별 이동 비용 계산
    n지점부터 목적지까지의 개별 이동 비용
  3. 총 이동 비용 계산 후 최솟값 갱신
    n지점까지의 합승 비용 + n~a의 이동 비용 + n~b의 이동 비용
"""
from heapq import heappush, heappop

# 그래프는 연결리스트 형태
def dijkstra(start, graph):
    # 초기화
    result = [float('inf')] * len(graph)    # 해당 지점까지의 비용
    result[start] = 0
    h = [(0, start)]    # 최소힙
    # 다익스트라
    while h:
        res_u, u = heappop(h)
        if res_u > result[u]:
            continue
        for v, w in graph[u]:
            if result[u] + w < result[v]:
                result[v] = result[u] + w
                heappush(h, (result[v], v))
    return result

def solution(n, s, a, b, fares):
    answer = float('inf')
    # 그래프를 연결리스트로 변환
    graph = [list() for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    # 합승 비용 계산
    result = dijkstra(s, graph)
    
    for mid in range(1, n+1):
        # 개별 이동 비용 계산
        a_result = dijkstra(mid, graph)[a]
        b_result = dijkstra(mid, graph)[b]
        # 총 이동 비용 계산 후 최솟값 갱신
        answer = min(answer, result[mid] + a_result + b_result)
        
    return answer
