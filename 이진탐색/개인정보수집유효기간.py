"""
[프로그래머스] 개인정보 수집 유효기간
https://school.programmers.co.kr/learn/courses/30/lessons/150370

- 약관 종류에 따라 수집 일자의 MM + 유효기간
- MM + 유효기간 > 12 -> (MM + 유효기간) % 12 하고, YYYY += (MM + 유효기간) // 12
- YYYY.MM.DD <= today -> 삭제

***
- YYYY / MM / DD 잘라서 비교하는 것보다 총 날짜 수를 더해 비교하는 것이 더 효율적
"""
def solution1(today, terms, privacies):
    answer = []
    
    periods = dict()    # <약관, 유효기간>
    for term in terms:
        name, period = term.split()
        periods[name] = int(period)
    
    for i in range(len(privacies)):
        date, name = privacies[i].split()
        y, m, d = date.split(".")
        
        # 유효기간 지난 후 날짜 계산
        m = int(m)
        m += periods[name]
        if m > 12:
            y = int(y)
            y += m // 12
            m = m % 12
            if m == 0:
                y -= 1
                m = 12
        
        m = str(m) if m >= 10 else "0" + str(m)
        expired = ".".join([str(y), m, d])
        
        # 파기 여부 검사
        if expired <= today:
            answer.append(i+1)
            
    return answer

def solution2(today, terms, privacies):
    answer = []
    
    y, m, d = map(int, today.split("."))
    today = y * 28 * 12 + m * 28 + d
    
    # periods = dict()
    # for term in terms:
    #     name, period = term.split()
    #     periods[name] = int(period) * 28
    
    periods = {term[0]: int(term[2:]) * 28 for term in terms}
    
    for i in range(len(privacies)):
        y, m, d = map(int, privacies[i][:-2].split("."))
        days = (y * 28 * 12 + m * 28 + d) + periods[privacies[i][-1]]
        if days <= today:
            answer.append(i+1)
    
    return answer

testcases = [
    [
        "2022.05.19", 
        ["A 6", "B 12", "C 3"], 
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    ],
    [
        "2020.01.01",
        ["Z 3", "D 5"],
        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    ],
    [
        "2021.01.01",
        ["A 1", "B 10", "C 12", "D 24", "E 65", "Z 100"],
        ["2019.01.01 D", "2019.11.15 B", "2000.08.02 Z", "2019.07.01 C", "2018.12.28 E"]
    ]
]

for testcase in testcases:
    print("answer:", solution1(testcase[0], testcase[1], testcase[2]))
