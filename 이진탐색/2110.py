"""
2110번 공유기 설치: https://www.acmicpc.net/problem/2110

**이진탐색** 탐색 데이터가 크면 일단 이진탐색 생각!!
- start: 1, end: 마지막 집 - 처음 집
- mid: 가장 인접한 두 공유기 사이 거리

***
- end: (마지막 집 - 처음 집) // (공유기 개수 - 1) + 1
- end를 바꾸니 소요 시간 절반됨
"""
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = [int(input().rstrip()) for _ in range(N)]

x.sort()
start = 1
end = (x[-1] - x[0]) // (C - 1) + 1

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    before_x = x[0]
    for i in range(1, len(x)):
        if x[i] - before_x >= mid:
            cnt += 1
            before_x = x[i]
        if cnt >= C:    # 해당 mid로 모든 공유기를 설치할 수 있으면
            start = mid + 1 # 거리 증가
            break
    else:   # 해당 mid로 모든 공유기를 설치할 수 없다면
        end = mid - 1   # 거리 감소
        
print(end)