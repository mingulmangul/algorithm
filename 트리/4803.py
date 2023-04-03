"""
4803번 트리: https://www.acmicpc.net/problem/4803
***
참고: https://imzzan.tistory.com/163
"""
import sys
from collections import deque

input = sys.stdin.readline


# node와 연결된 정점들이 사이클을 생성하는지 체크
def is_cycle(visited, graph, node):
    q = deque([node])
    visited[node] = True
    flag = False
    while q:
        u = q.popleft()
        for v in graph[u]:
            if visited[v]:  # 이미 방문한 노드를 재방문 -> 사이클이 존재
                flag = True
                continue
            graph[v].remove(u)
            q.append(v)
            visited[v] = True
    return flag


t = 1
n, m = map(int, input().split())
while n != 0 or m != 0:
    # 그래프 입력
    graph = {key: set() for key in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)

    # 모든 연결 요소 방문
    visited = [False] * (n + 1)
    tree_num = 0
    for node in graph.keys():
        # 사이클이 생성되지 않은 경우 카운팅
        if not visited[node] and not is_cycle(visited, graph, node):
            tree_num += 1

    # 출력
    if tree_num == 0:
        msg = "No trees."
    elif tree_num == 1:
        msg = "There is one tree."
    else:
        msg = f"A forest of {tree_num} trees."
    print(f"Case {t}: {msg}")

    # 다음 테스트 케이스 입력
    t += 1
    n, m = map(int, input().split())
