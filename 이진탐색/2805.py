"""
2805번: 나무 자르기
https://www.acmicpc.net/problem/2805

- 절단기 높이의 최댓값을 이진탐색으로 구하기
- start: 0, end: 가장 긴 나무 길이 - 1

***
조건을 만족하는 최댓값 구하기
- 조건을 만족하는 값을 찾았다고 바로 리턴 X. 최댓값을 찾기 위해 start를 오른쪽으로 이동
- [0, end] 범위의 값이 답으로 가능함
=> 탐색이 끝났을 때, end가 최종 답 (mid가 답이 아님!)

참고: https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2805%EB%B2%88.-%EB%82%98%EB%AC%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0
"""
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees) - 1

while start <= end:
    mid = (start + end) // 2
    total = sum([tree - mid for tree in trees if tree >= mid])
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)