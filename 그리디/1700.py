"""
1700번: 멀티탭 스케줄링
https://www.acmicpc.net/problem/1700

1. 비어있으면, 꽂기
2. 그렇지 않으면,
    2-1. 앞으로 사용하지 않는 전기용품 뽑기
    2-2. 없으면, 가장 나중에 다시 사용되는 것 뽑기
    
풀이 참고: https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-1700%EB%B2%88-%EB%A9%80%ED%8B%B0%ED%83%AD-%EC%8A%A4%EC%BC%80%EC%A5%B4%EB%A7%81

단순하게 <최종 사용 순서가 가장 이른 것 뽑기>, <가장 마지막에 사용되는 것 뽑기>를 최적해로 생각했는데 반례가 있었다
- 반례 1
    2 15
    3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
- 반례 2
    3 13
    1 2 3 4 1 2 3 2 3 4 2 3 1
실제 최적해는 <가장 나중에 재사용되는 것 뽑기>였다
해당 제품이 다시 사용될 때까지는 
해당 제품을 고려하지 않아도 되고, 나머지 꽂혀있는 제품을 계속 재사용할 수 있기 때문이다
"""
N, K = map(int, input().split())
arr = list(map(int, input().split()))

multitab = set()
cnt = 0
for i in range(0, len(arr)):
    # 멀티탭에 자리가 없다면
    if arr[i] not in multitab and len(multitab) >= N:
        # 가장 나중에 다시 사용되는 제품 찾기
        temp = set(multitab)
        target = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] in temp:
                target = arr[j]
                temp.remove(arr[j])
            if not temp:
                break
        
        # 다시 사용되지 않는 제품이 있는지 찾기
        if temp:
            target = temp.pop()
        
        # 플러그 뽑기
        multitab.remove(target)
        cnt += 1
            
    # 플러그 꽂기
    multitab.add(arr[i])
    
print(cnt)