"""
16026번: 롤케이크
https://www.acmicpc.net/problem/16206

- 10으로 나누어 떨어지는 롤케이크를 우선 자름 (잘랐을 때, 10 10이 되는 경우)
    - 이 중에서는 길이가 짧은 것부터 우선 자름
- 나머지 롤케이크를 잘라서 10을 만듦
"""
# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

# A.sort()
A.sort(key=lambda x: (x % 10, x))

cake = 0
for x in A:
    # X를 자를 수 있는 횟수 계산
    cut = (x - 1) // 10
    if M < cut:
        cut = M
    
    # 계산한 횟수만큼 잘랐을 때 케이크 개수 계산
    cake += cut
    if x - 10 * cut == 10:
        cake += 1
        
    M -= cut
    if M == 0:
        break

print(cake)