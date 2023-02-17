"""
15661번: 링크와 스타트
https://www.acmicpc.net/problem/15661

- 한 팀당 팀원 수 : [2, N-2]
- 조합 구하기 -> [:i] / [i+1:] 로 팀 나누기
"""
import sys, itertools
input = sys.stdin.readline

N = int(input().rstrip())
S = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")

def calc_stat(S, team):
    stat = 0
    for m1, m2 in itertools.combinations(team, 2):
        stat += S[m1][m2] + S[m2][m1]
    return stat

for i in range(2, (N // 2) + 1):
    combs = list(itertools.combinations(range(N), i))
    for team1 in combs:
        stat1 = calc_stat(S, team1)
        team2 = [x for x in range(N) if x not in team1]
        stat2 = calc_stat(S, team2)
        answer = min(answer, abs(stat1 - stat2))
        
print(answer)

"""
# 시간초과
visited = [0] * N

def calc_stat2():
    global answer
    team1, team2 = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                team1 += S[i][j]
            elif not visited[i] and not visited[j]:
                team2 += S[i][j]
    answer = min(answer, abs(team1 - team2))

def iter(cnt):
    if cnt == N:
        calc_stat2()
        return
    visited[cnt] = 1
    iter(cnt + 1)
    visited[cnt] = 0
    iter(cnt + 1)

iter(0)
print(answer)
"""
