"""
13305번: 주유소
https://www.acmicpc.net/problem/13305

- 다음 도시에 갈 때 최소 주유 비용 = min(현재 도시에 올 때까지의 최소 기름값(리터당 가격), 현재 도시의 기름값) * 다음 도시와의 거리

"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

res = road[0] * price[0]
min_price = price[0]

for i in range(1, N-1):
    min_price = min(min_price, price[i])
    res += min_price * road[i]

print(res)