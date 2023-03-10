"""
양궁대회: https://school.programmers.co.kr/learn/courses/30/lessons/92342

브루트포스 (DFS)
***
구현 잘 했는데 가장 낮은 점수를 더 많이 맞힌 경우를 리턴하기 위해 answer를 정렬해야 하는 걸 생각 못했다..
참고: https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-Python
"""
answer = []
score = 0
    
# 어피치, 라이언 점수 차 계산하기
def calc_score(a_info, l_info):
    a_score, l_score = 0, 0
    for i in range(0, 10):
        if a_info[i] < l_info[i]:
            l_score += (10 - i)
        elif a_info[i] > 0:
            a_score += (10 - i)
    return l_score - a_score

def dfs(idx, arrow, a_info, l_info):
    global answer, score
    # 끝까지 탐색했거나 n발을 모두 쏜 경우
    if idx >= 10 or arrow == 0:
        # 점수 차 계산 후 정답 갱신
        new_score = calc_score(a_info, l_info)
        if new_score > score:
            score = new_score
            answer = [l_info[:]]
        elif new_score == score and score > 0:
            answer.append(l_info[:])
        return
    
    for i in range(idx, 10):
        num = a_info[i] + 1
        # 해당 점수를 라이언이 남은 화살로 가져갈 수 있다면
        if num <= arrow:
            l_info[i] = num  # 해당 점수를 가져가고
            dfs(i + 1, arrow - num, a_info, l_info)   # dfs 실행
            l_info[i] = 0
            
    l_info[10] = arrow
    dfs(10, arrow, a_info, l_info)
    l_info[10] = 0
                
def solution(n, info):
    dfs(0, n, info, [0] * 11)
    if not answer:
        return [-1]
    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]