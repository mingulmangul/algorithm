"""
12852번: 1로 만들기 2
https://www.acmicpc.net/problem/12852

- BFS
- 가장 먼저 1을 만드는 루트를 출력
 → 시간 초과
- DP : 직전 노드를 저장

***
- print(" ".join(arr)) == print(*arr)
- 다른 풀이 : https://www.acmicpc.net/source/55698858
"""
from collections import deque
N = int(input())

# 시간 초과
def solution1(N):
    q = deque([[N]])
    
    while q:
        route = q.popleft()
        n = route[-1]
        if n == 1:
            print(len(route) - 1)
            print(" ".join(map(str, route)))
            return
        if n % 3 == 0:
            q.append(route + [n // 3])
        if n % 2 == 0:
            q.append(route + [n // 2])
        q.append(route + [n - 1])
        
# DP 배열에 직전 노드 저장 + 이미 방문했으면 pass
def solution2(N):
    q = deque([N])
    dp = [0] * (N+1)
    while q:
        n = q.popleft()
        # 1에 도착했으면
        if n == 1:
            # N까지 거슬러 올라가기
            answer = deque([n])
            while n != N:
                n = dp[n]
                answer.appendleft(n)
            # 출력
            print(len(answer) - 1)
            print(*answer)
            return
        
        # 아직 방문한 적 없으면, 방문 + 직전 노드 저장
        if n % 3 == 0 and dp[n//3] == 0:
            dp[n//3] = n
            q.append(n//3)
        if n % 2 == 0 and dp[n//2] == 0:
            dp[n//2] = n
            q.append(n//2)
        if dp[n-1] == 0:
            dp[n-1] = n
            q.append(n-1)
            
# solution1(N)
solution2(N)