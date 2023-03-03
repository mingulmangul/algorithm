"""
5397번 키로거: https://www.acmicpc.net/problem/5397

- 문자: 비밀번호 덱 append
- 백스페이스: 비밀번호 덱 pop
- 왼쪽 화살표: 비밀번호 덱 pop + 스택에 push
- 오른쪽 화살표: 스택 pop + 비밀번호 덱 append
"""
import sys
from collections import deque
input = sys.stdin.readline

# 내 풀이 (1432ms)
T = int(input().rstrip())
for _ in range(T):
    key = input().rstrip()
    password = deque()
    stack = deque()
    for ch in key:
        if ch == '-':
            if password:
                password.pop()
        elif ch == '<':
            if password:
                stack.append(password.pop())
        elif ch == '>':
            if stack:
                password.append(stack.pop())
        else:
            password.append(ch)
        
    stack.reverse()
    print(*password, *stack, sep="")