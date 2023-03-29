"""
불량 사용자: https://school.programmers.co.kr/learn/courses/30/lessons/64064

DFS
- 제재 아이디 -> 제재 아이디가 될 수 있는 아이디 목록 매핑
- 각 목록 당 아이디 하나씩 선택해서 조합 만들기 (DFS)
- 중복 제거

**
- product 또는 permutation을 사용하면 쉽게 조합을 구할 수 있음!
"""
from itertools import product

# 내 풀이 (DFS로 조합 선택)
# 가장 시간이 오래걸리는 테스트 5번에서 47.77ms
banned_list = []


def select_id(candidates, selections, cnt):
    if cnt == len(candidates):
        if selections not in banned_list:
            banned_list.append(selections)
        return

    for candidate in candidates[cnt]:
        if candidate not in selections:
            select_id(candidates, selections | {candidate}, cnt + 1)


def solution(user_id, banned_id):
    candidates = [[] for _ in range(len(banned_id))]

    # 제재 아이디 - [제재 아이디가 될 수 있는 아이디 목록] 매핑
    for idx, bid in enumerate(banned_id):
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            for i in range(len(bid)):
                if bid[i] != "*" and bid[i] != uid[i]:
                    break
            else:
                candidates[idx].append(uid)

    # 조합 선택
    select_id(candidates, set(), 0)

    return len(banned_list)


# 추가 풀이 (product 함수로 조합 선택)
# 테스트 5번에서 6123.84ms
def solution2(user_id, banned_id):
    candidates = [[] for _ in range(len(banned_id))]

    # 제재 아이디 - [제재 아이디가 될 수 있는 아이디 목록] 매핑
    for idx, bid in enumerate(banned_id):
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            for i in range(len(bid)):
                if bid[i] != "*" and bid[i] != uid[i]:
                    break
            else:
                candidates[idx].append(uid)

    # 조합 선택
    combs = product(*candidates)
    for comb in combs:
        comb = set(comb)
        if len(comb) == len(banned_id) and comb not in banned_list:
            banned_list.append(comb)

    print(banned_list)
    return len(banned_list)


print(solution2(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                ["fr*d*", "*rodo", "******", "******"]))
