"""
2295번: 세 수의 합
https://www.acmicpc.net/problem/2295

- 중간에서 만나기
(k - x) 모든 경우의 수 저장해두기 -> N^2 (k가 가장 큰 경우만 저장)
(y + z) 모든 경우의 수와 (k - x) 비교 -> N^2
비교해서 같은 경우의 k 중 최댓값 출력
O(N^2) => 1,000,000

***
- (y + z)를 먼저 계산 + set에 저장해두면, 복잡하게 dictionary 사용할 필요 X
- 원소 2개를 뽑아 모든 경우의 수를 만드는 코드 -> 조합 라이브러리 사용 가능
- 참고
     - https://www.acmicpc.net/source/41673564
     - https://www.acmicpc.net/source/51292603
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
U = set([int(input().rstrip()) for _ in range(N)])

k_sub_x = dict()  # <(k - x), k> 저장
for k in U:
    for x in U:
        sub = k - x
        # <(k - x), k>가 없으면 k 저장, 있으면 더 큰 k 저장
        if sub >= 0 and k_sub_x.setdefault(sub, k) < k:
            k_sub_x[sub] = k

max_k = 0   # 가장 큰 k
for y in U:
    for z in U:
        # (y + z) == (k - x)인 y, z가 있는지 확인
        add = y + z
        k = k_sub_x.get(add)
        # 최댓값 갱신
        if k and k > max_k:
            max_k = k

print(max_k)
"""
import itertools
import sys
input = sys.stdin.readline

N = int(input().rstrip())
U = set([int(input().rstrip()) for _ in range(N)])

add = {x + y for x, y in itertools.combinations_with_replacement(U, 2)}

arr = sorted(U)
for k in range(N-1, 0, -1):
    for z in range(k):
        if arr[k] - arr[z] in add:
            print(arr[k])
            exit()
"""