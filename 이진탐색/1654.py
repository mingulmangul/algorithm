"""
1654번: 랜선 자르기
https://www.acmicpc.net/problem/1654

- 이진탐색으로 랜선을 자를 길이 찾기
- 이진탐색 -> start: 1, end: 가장 긴 랜선 길이

*** 참고
- start: 1, end: 랜선 길이 총합 // N
- list 원소 모두 더할 때 sum() 내장 함수 사용
"""
"""
def calc_n(arr, cut):
    n = 0
    for x in arr:
        n += x // cut
    return n

def binary_search(arr, N):
    start = 1
    end = max(arr)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cur_n = calc_n(arr, mid)
        
        if cur_n >= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result    
    
K, N = map(int, input().split())
lines = [int(input().rstrip()) for _ in range(K)]
print(binary_search(lines, N))
"""
import sys
input = sys.stdin.readline
    
K, N = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(K)]

start = 1
end = sum(arr) // N

while start <= end:
    mid = (start + end) // 2
    if sum([x // mid for x in arr]) >= N:
        start = mid + 1
    else:
        end = mid - 1
            
print(end)