"""
15681번 트리와 쿼리: https://www.acmicpc.net/problem/15681

트리(재귀/DFS), DP
- 그래프 입력 받기
- 재귀적으로 트리 만들며 서브 트리 정점 개수 카운트

***
- 재귀 없이 BFS를 이용한 풀이도 가능
참고: https://www.acmicpc.net/source/55616679
"""
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
# 그래프 입력 받기
tree = dict()
for _ in range(N - 1):
    u, v = map(int, input().split())
    if u in tree:
        tree[u].add(v)
    else:
        tree[u] = {v}
    if v in tree:
        tree[v].add(u)
    else:
        tree[v] = {u}

# 재귀적으로 트리 만들며 서브 트리 정점 개수 카운트
def make_tree(tree, size, node, parent):
    for v in tree[node]:
        if v == parent:
            continue
        size[node] += make_tree(tree, size, v, node)
    return size[node]


# 트리 만들며 각 노드를 루트로 하는 서브 트리의 정점 개수 카운트
size = [1] * (N + 1)
make_tree(tree, size, R, 0)

# 출력
for _ in range(Q):
    root = int(input().rstrip())
    print(size[root])
