"""
문자열 압축: https://level.goorm.io/exam/100821/15%ED%9A%8C-epper-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95/quiz/1

문자열
- 시작 비트가 1이면, 문자열 1로 시작
- 이전 문자와 같은 문자면 카운팅
- 이전 문자와 다른 문자면 카운팅한 값 문자열에 추가
"""
src = input()

prev = src[0]
answer = "1" if prev == "1" else ""

cnt = 0
for i in range(1, len(src)):
    if src[i] == prev:
        cnt += 1
    else:
        answer += chr(ord("A") + cnt)
        prev = src[i]
        cnt = 0

answer += chr(ord("A") + cnt)
print(answer)
