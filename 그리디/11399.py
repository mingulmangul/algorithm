"""
11399번: ATM
https://www.acmicpc.net/problem/11399

- SJF -> 정렬
- sum(i번 사람이 인출하는 시간(== 0~i번의 인출 시간의 합))

***
- sum(i번 사람이 인출하는 시간 * (사람 수 - i))
"""
N = int(input())
P = sorted(list(map(int, input().split())))

# 내 풀이
def solution1():
    answer = 0
    for i in range(1, N+1):
        answer += sum(P[:i])
    print(answer)

# 추가 풀이
def solution2():
    answer = 0
    for i in range(N):
        answer += P[i] * (N - i)
    print(answer)
    
solution1()
solution2()