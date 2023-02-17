"""
1759번: 암호 만들기
https://www.acmicpc.net/problem/1759

- 모음 자음 분리
- 조합 만들기: 모음에서 i개 자음에서 L-i개 선택 (i >= 1)
- 오름차순 정렬 후 출력

***
- 자음, 모음 분리해서 조합 뽑을 필요 X
- 전체 알파벳을 정렬 후 조합을 뽑으면 나중에 정렬할 필요 X
"""
from itertools import combinations
L, C = map(int, input().split())

def solution1():
    consonant = []
    vowel = []
    answer = []

    for alpha in input().split():
        if alpha in ('a', 'e', 'i', 'o', 'u'):
            vowel.append(alpha)
        else:
            consonant.append(alpha)

    for i in range(1, len(vowel) + 1):
        if len(consonant) < L - i or L - i < 2:
            continue
        selected_v = list(combinations(vowel, i))
        selected_c = list(combinations(consonant, L-i))
        for sv in selected_v:
            for sc in selected_c:
                answer.append(sorted(sv+sc))

    print("\n".join(map("".join, sorted(answer))))

def solution2():
    arr = sorted(input().split())

    for comb in combinations(arr, L):
        vowel_cnt = 0
        for alpha in comb:
            if alpha in ('a', 'e', 'i', 'o', 'u'):
                vowel_cnt += 1
        
        if vowel_cnt >= 1 and L - vowel_cnt >= 2:
            print("".join(comb))