"""
양과 늑대: https://school.programmers.co.kr/learn/courses/30/lessons/92343
- (선택된 경로) [방문한 노드 집합] / [갈 수 있는 노드 집합] 양:늑대
    [0] / [1 2]
    [0 2] / [1 5 6]
    [0 2 5] / [1 6] (양 우선 선택)
    (1) [0 2 5 1] / [6 3 4]
        (1-6) [0 2 5 1 6] / [3 4 9] 3:2 -> fail (갈 수 있는 곳이 없음)
        (1-3) [0 2 5 1 3] / [6 4 7]
              [0 2 5 1 3 7] / [6 4] 4:2
              (1-3-6) [0 2 5 1 3 7 6] / [4 9] 4:3 -> fail
              (1-3-4) [0 2 5 1 3 7 4] / [6 8] 4:3
                      [0 2 5 1 3 7 4 8] / [6] 5:3
                      [0 2 5 1 3 7 4 8 6] / [9] 5:4 -> fail
        (1-4) [0 2 5 1 4] / [6 3 8]
              [0 2 5 1 4 8] / [6 3] 4:2
              (1-4-6) [0 2 5 1 4 8 6] / [3 9] 4:3 -> fail
              (1-4-3) [0 2 5 1 4 8 3] / [6 7] 4:3
                      [0 2 5 1 4 8 3] / [6] 5:3
                      [0 2 5 1 4 8 3 6] / [9] 5:4 -> fail
    최종답: 5

1. 노드 방문
    - 양 우선 선택 -> 양의 수 최댓값 갱신
    - 모든 노드 방문
    - 갈 수 있는 곳이 더 없으면 종료
2. 갈 수 있는 곳 추가
"""
answer = 1

def search(info, sheep, wolf, next_nodes, edge_list):
    global answer
    for next_node in next_nodes:
        # 갈 수 있는 노드 중에 양이 있으면 바로 방문
        if info[next_node] == 0:
            next_nodes.remove(next_node)
            answer = max(answer, sheep + 1)
            new_next_nodes = next_nodes + edge_list[next_node]  # 새로 갈 수 있는 노드 추가
            search(info, sheep + 1, wolf, new_next_nodes, edge_list)  
            return
    # 늑대 수가 많아져 더이상 갈 수 있는 곳이 없으면 종료
    if sheep - wolf == 1:
        return
    # 다른 노드 하나씩 방문
    for i in range(len(next_nodes)):
        new_next_nodes = next_nodes[:i] + next_nodes[i+1:] + edge_list[next_nodes[i]]
        search(info, sheep, wolf+1, new_next_nodes, edge_list)

def solution(info, edges):
    # 입력 처리
    edge_list = [[] for _ in range(len(info))]
    for parent, child in edges:
        edge_list[parent].append(child)
    # 초기화
    search(info, 1, 0, edge_list[0], edge_list)
    return answer
