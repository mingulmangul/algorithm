"""
1931번: 회의실 배정
https://www.acmicpc.net/problem/1931

-- 내 풀이 --
1. 회의실이 비어있다면, i번째 회의 시작
2. 그렇지 않다면, 
    진행 중인 회의보다 i번째 회의가 빨리 끝난다면, i번째 회의로 교체

-- 다른 사람의 풀이 --
1. 끝나는 시간이 빠른 순으로 정렬
2. 회의실이 비어있다면, i번째 회의 시작
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = sorted([list(map(int, input().split())) for _ in range(N)])

min_end = arr[0][1]
cnt = 1
for i in range(1, N):
    if min_end <= arr[i][0]: # 회의실이 비어있다면
        min_end = arr[i][1]  # i번째 회의 시작
        cnt += 1
    elif min_end > arr[i][1]:   # 진행 중인 회의보다 i번째 회의가 빨리 끝난다면
        min_end = arr[i][1]     # 진행 중인 회의 교체

print(cnt)