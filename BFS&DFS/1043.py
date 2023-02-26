"""
1043번: 거짓말
https://www.acmicpc.net/problem/1043

- 진실을 아는 사람이 참가하는 파티를 모두 제외

***
1. 집합 
참고: https://www.acmicpc.net/source/54760044
2. 유니온 파인드
참고:
https://seongonion.tistory.com/131 
https://velog.io/@dasd412/백준-1043-거짓말-파이썬
"""
import sys
input = sys.stdin.readline

### 내 풀이
def solution():    
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    parties = [list(map(int, input().split()))[1:] for _ in range(M)]

    truth = set()  # 진실을 아는 사람들
    for i in range(1, len(data)):
        truth.add(data[i])

    cnt = M  # 거짓말을 할 수 있는 파티 수
    checked = [False] * M  # 파티 탐색 여부 체크
    while truth:
        t = truth.pop()
        # 진실을 아는 사람이 참가하는 파티를 모두 제외
        for i in range(len(parties)):
            if not checked[i] and t in parties[i]:
                cnt -= 1
                checked[i] = True
                # 새로 진실을 알게 된 사람 추가
                for person in parties[i]:
                    if person != t:
                        truth.add(person)
    return cnt              

# print(solution())

### 집합
def solution1():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    parties = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
    
    truth = set()  # 진실을 아는 사람들
    for i in range(1, len(data)):
        truth.add(data[i])
    
    # 진실을 아는 사람을 모두 같은 집합으로 합침
    for _ in range(N):
        for party in parties:
            if party & truth:   # 교집합
                truth |= party  # 합집합
    
    cnt = 0  # 거짓말을 할 수 있는 파티 수
    for party in parties:
        if party & truth:
            continue
        cnt += 1
    return cnt

# print(solution1())

### 유니온 파인드
### union 연산에서 루트 노드의 parent가 아닌 자식 노드의 parent만 변경해서 실패
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution2():
    N, M = map(int, input().split())
    truth = list(map(int, input().split()))[1:]
    
    # 진실을 아는 집합은 루트 노드가 0인 집합으로 표시
    parent = list(range(N+1))
    for person in truth:
        parent[person] = 0
    
    parties = []
    for _ in range(M):
        party = list(map(int, input().split()))[1:]
        # 같은 파티의 사람들을 모두 같은 집합으로 합침
        for i in range(len(party) - 1):
            union(parent, party[i], party[i+1])
        parties.append(party)
    
    cnt = 0  # 거짓말을 할 수 있는 파티 수
    for party in parties:
        for p in party:
            if find(parent, p) == 0:
                break
        else:
            cnt += 1
    return cnt

print(solution2())