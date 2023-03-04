"""
이중 우선순위 큐 https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""
from collections import deque

def solution(operations):
    dq = deque()
    for op in operations:
        if op[0] == 'I':
            dq.append(int(op[2:]))
            dq = deque(sorted(dq))
        elif op[2] == '-' and dq:
            dq.popleft()
        elif op[2] == '1' and dq:
            dq.pop()
    if not dq:
        return [0, 0]
    return [dq[-1], dq[0]]

operations = [
    ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]]

for op in operations:
    print(solution(op))