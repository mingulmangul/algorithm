"""
3 x n 타일링: https://school.programmers.co.kr/learn/courses/30/lessons/12902

- 가로 2칸을 채우는 경우의 수 : 3
- 가로 4칸을 채우는 경우의 수 : 2
- 가로 6칸을 채우는 경우의 수 : 2
- 가로 8칸을 채우는 경우의 수 : 2
- ...
- s(n) = s(n - 2) * 3 + s(n - 4) * 2 + s(n - 6) * 2 + ...

"""
def solution(n):
    if n % 2 != 0:
        return 0
    arr = [0] * (n + 1)
    arr[0] = 1
    arr[2] = 3
    for i in range(4, n+1, 2):  # 짝수만 체크!! (1100 -> 230)
        # 모듈러 연산 단계마다 수행 (230 -> 110)
        arr[i] = (arr[i-2] * 3 + sum([arr[x] for x in range(0, i-2, 2)]) * 2) % 1000000007
    return arr[n]

print(solution(4))
