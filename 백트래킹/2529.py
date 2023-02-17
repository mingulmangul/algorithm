"""
2529번: 부등호
https://www.acmicpc.net/problem/2529

- 브루트포스.. 백트래킹!
- eval() 내장함수 사용
"""
K = int(input())
arr = list(input().split())

answer = []
visited = [False] * 10

def solution(arr, visited, number, cnt):
    if cnt >= K:
        answer.append(number)
        return
    for num in range(10):
        if cnt < 0 or (not visited[num] and eval(number[-1] + arr[cnt] + str(num))):
            visited[num] = True
            solution(arr, visited, number + str(num), cnt + 1)
            visited[num] = False

solution(arr, visited, "", -1)
print(answer[-1], answer[0], sep="\n")