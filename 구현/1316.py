"""
1316번: 그룹 단어 체커
https://www.acmicpc.net/problem/1316

- 문자 셋에 저장
- 문자가 연속되는지 확인 -> O
- 아니라면 셋에 있는지 확인(이전에 나온적 있는지) -> X

***
- list(word) != sorted(word, key=word.find) -> X
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
words = [input().rstrip() for _ in range(N)]

cnt = 0
for word in words:
    s = set(word[0])
    for i in range(1, len(word)):
        if word[i-1] != word[i] and word[i] in s:
            break
        s.add(word[i])
    else:
        cnt += 1

print(cnt)