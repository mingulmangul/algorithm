"""
성적평가: https://softeer.ai/practice/info.do?idx=1&eid=1309

- (점수, 번호) 내림차순 정렬 -> O(nlogn)
- 정렬 후 등수 계산 -> O(n)
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
total_score = [0] * N
for idx in range(4):
    if idx < 3:
        scores = list(map(int, input().split()))
    else:
        scores = total_score
    # (점수, 참가자 번호) 내림차순 정렬    
    data = []
    for i, score in enumerate(scores):
        data.append((score, i))
        if idx < 3:
            total_score[i] += score
    data.sort(reverse=True)
    # 등수 계산
    rank = [1] * N
    for i in range(1, len(data)):
        if data[i][0] == data[i-1][0]:
            rank[data[i][1]] = rank[data[i-1][1]]
        else:
            rank[data[i][1]] += i
    print(*rank)
    