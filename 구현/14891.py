"""
14891번 톱니바퀴: https://www.acmicpc.net/problem/14891
- 구현
"""
import sys
input = sys.stdin.readline

################################
# 톱니바퀴를 클래스로 처리한 풀이
################################


class wheel:
    # 테스트용 출력
    def __str__(self):
        temp = self.state[self.top:] + self.state[:self.top]
        return str(temp)

    def __init__(self, data):
        self.state = [x for x in data]  # 톱니바퀴 극 상태 정보
        self.top = 0                    # 12시 방향의 인덱스

    def get_left(self):
        return self.state[(self.top + 6) % 8]   # 왼쪽의 극 리턴

    def get_right(self):
        return self.state[(self.top + 2) % 8]   # 오른쪽의 극 리턴

    def turn(self, direction):
        if direction == -1:                 # 반시계방향 회전
            self.top = (self.top + 1) % 8   # 12시 방향의 인덱스를 모듈러 연산
        elif direction == 1:                # 시계방향 회전
            self.top = (self.top + 7) % 8


info = [input().rstrip() for _ in range(4)]
wheels = [wheel(data) for data in info]
K = int(input().rstrip())
for _ in range(K):
    target, direction = map(int, input().split())
    target -= 1

    directions = [0] * 4    # 각 톱니바퀴가 회전해야 할 방향
    directions[target] = direction
    # 오른쪽에 있는 톱니바퀴 중 회전해야 하는 톱니바퀴가 있는지 확인
    for i in range(target, 3):
        if wheels[i].get_right() != wheels[i + 1].get_left():
            direction = -direction  # 맞물린 톱니바퀴와 반대방향으로 회전
            directions[i + 1] = direction
        else:
            break
    # 왼쪽에 있는 톱니바퀴 중 회전해야 하는 톱니바퀴가 있는지 확인
    direction = directions[target]
    for i in range(target, 0, -1):
        if wheels[i].get_left() != wheels[i - 1].get_right():
            direction = -direction
            directions[i - 1] = direction
        else:
            break
    # 방향에 따라 톱니바퀴 회전
    for i in range(4):
        wheels[i].turn(directions[i])

# 출력
# 12시 방향이 S극(1)인 경우에만 점수 획득
print(sum([2**i for i in range(4) if wheels[i].state[wheels[i].top] == '1']))


################################
# 톱니바퀴를 문자열로 처리한 풀이
################################
"""
wheels = [input().rstrip() for _ in range(4)]
K = int(input().rstrip())

for _ in range(K):
    target, direction = map(int, input().split())
    rotation = [0] * 4  # rotation[i] : i번째 톱니바퀴의 회전할 방향
    rotation[target-1] = direction
    # 오른쪽 톱니바퀴 확인
    for i in range(target-1, 3):
        # 현재 톱니바퀴의 오른쪽 != 오른쪽 톱니바퀴의 왼쪽
        if wheels[i][2] != wheels[i+1][6]:
            # 오른쪽 톱니바퀴 회전
            rotation[i+1] = -rotation[i]
        else:
            break
    # 왼쪽 톱니바퀴 확인
    for i in range(target-1, 0, -1):
        # 현재 톱니바퀴의 왼쪽 != 왼쪽 톱니바퀴의 오른쪽
        if wheels[i][6] != wheels[i-1][2]:
            rotation[i-1] = -rotation[i]
        else:
            break

    # 실제 회전
    for i in range(4):
        if rotation[i] != 0:
            top = 1 if rotation[i] == -1 else 7
            wheels[i] = wheels[i][top:] + wheels[i][:top]

# 점수 계산
print(sum([int(wheels[i][0]) * 2 ** i for i in range(4)]))
"""
