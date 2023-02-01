"""
11047번: 동전 0
https://www.acmicpc.net/problem/11047

1. 가장 가치(<= K)가 큰 동전 선택
2. K에서 선택한 동전의 가치만큼을 뺌
3. K가 0이 될 때까지 반복
"""

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N-1, -1, -1):
    cnt += K // coins[i]
    K %= coins[i]
    if K == 0:
        break
print(cnt)