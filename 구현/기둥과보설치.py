"""
기둥과 보 설치: https://school.programmers.co.kr/learn/courses/30/lessons/60061

구현 문제
- 입력 build_frame = [ [x, y, 0:기둥 1:보, 0:삭제 1:설치] ]
- 출력 arr = [ [x, y, 0:기둥 1:보] ] (오름차순 정렬)
- 기둥: 보의 한쪽 끝 위에, 다른 기둥 위에, 바닥 위에
- 보: 한쪽 끝이 기둥 위에, 양쪽 끝이 다른 보와 연결

***
삭제/설치 후 주변 구조물이 규칙을 만족하는지 모든 조건을 if-else로 체크하다가 훨씬 좋은 풀이를 발견..
설치의 경우 주변 구조물의 규칙 만족 여부를 확인하기 쉽지만, 삭제는 그렇지 않음
  -> 전체 구조물을 다시 탐색하기
참고: https://blackon29.tistory.com/65
"""
def is_valid(structures):
    for x, y, structure in structures:
        if structure == 0:  # 기둥
            if y > 0 and (x, y-1, 0) not in structures \
                and (x-1, y, 1) not in structures and (x, y, 1) not in structures:
                return False
        else:   # 보
            if ((x-1, y, 1) not in structures or (x+1, y, 1) not in structures) \
                and ((x, y-1, 0) not in structures and (x+1, y-1, 0) not in structures):
                return False
    return True

def solution(n, build_frame):
    structures = set()
    for x, y, structure, method in build_frame:
        elem = (x, y, structure)
        if method == 1:
            structures.add(elem)
            if not is_valid(structures):
                structures.remove(elem)
        else:
            structures.remove(elem)
            if not is_valid(structures):
                structures.add(elem)
    
    return sorted(list(structures))


# 테스트 입력
n = [5, 5]
build_frame = [[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
               [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]]
i = 1
print(solution(n[i], build_frame[i]))