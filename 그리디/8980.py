"""
8980번: 택배
https://www.acmicpc.net/problem/8980

- 받는 마을 번호가 작은 것부터 우선 배달(트럭에 싣기)
- 받는 마을 번호가 같으면, 보내는 마을 번호가 작은 것부터 우선 배달
 
풀이 참고: https://www.acmicpc.net/board/view/6327
"""
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input().rstrip())
data = [list(map(int, input().split())) for _ in range(M)]
box = [C] * (N + 1)

data.sort(key=lambda x: (x[1], x[0]))
res = 0
for s, e, b in data:
    capacity = min(C, min(box[s:e]))
    carry = min(b, capacity)
    for i in range(s, e):
        box[i] -= carry
    res += carry

print(res)