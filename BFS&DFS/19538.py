"""
19538번 루머: https://www.acmicpc.net/problem/19538

BFS
- 새로 루머를 믿게 된 사람의 시간 = 유포자가 루머를 믿기 시작한 시간 + 1
- 새로 계산한 값이 더 작을 때에만 갱신
- 주변인 절반 이상이 루머를 믿을 때 믿게 됨!

***
- 새로 계산한 값이 더 작을 때에만 갱신 -> XX. BFS이기 때문에 visited로 갱신 여부 체크하면 됨
- 주변인 절반 이상이 감염됐는지 알기 위해 count[]를 정의하기!! 
    주변인이 감염될 때마다 -1, count가 0이 되면 해당 사람도 감염됨
참고: https://hoit1302.tistory.com/157
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
R = [list(map(int, input().split())) for _ in range(N)]
M = int(input().rstrip())
speaker = deque(map(int, input().split()))
time = [-1] * N
count = [len(R[i]) // 2 for i in range(N)]   # 주변인의 수 // 2

for s in speaker:
    time[s-1] = 0

while speaker:
    s = speaker.popleft() - 1

    for r in R[s]:
        if r == 0:
            break
        r -= 1
        if time[r] >= 0:    # 이미 감염된 사람은 패스
            continue
        count[r] -= 1
        if count[r] == 0:   # 0이 되면(주변인의 절반 이상이 감염되면)
            # 감염됨
            time[r] = time[s] + 1
            speaker.append(r + 1)

print(*time)
