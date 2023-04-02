""""
5639번 이진 검색 트리: https://www.acmicpc.net/problem/5639

***
- ^Z(EOF)가 마지막 입력이므로 try-except문 사용
- 전위 순회 입력을 3부분으로 나눌 수 있음
- 루트 / 왼쪽 자식 트리 / 오른쪽 자식 트리
  -> 재귀적으로 다시 3부분으로 나눌 수 있음
참고: https://ku-hug.tistory.com/132
***
- 파이썬의 경우, 최대 재귀 횟수 제한을 늘려야 함
- skewed tree인 경우 처리!! (1888ms -> 56ms)
  왼쪽/오른쪽 서브 트리 구분하는 인덱스 찾기 X, 루트를 제외하고 바로 재귀 호출
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 전위 순회 입력 받기
tree = []
while True:
    try:
        v = int(input().rstrip())
        tree.append(v)
    except:
        break

# 후위 순회하기 (재귀)
def postorder(tree, start, end):
    if start >= end - 1:
        print(tree[start])
        return

    if tree[start] < tree[start + 1] or tree[start] > tree[end - 1]:
        # skewed tree인 경우, 루트를 제외하고 바로 재귀 호출
        postorder(tree, start + 1, end)
    else:
        # 왼쪽/오른쪽 서브 트리 구분하는 인덱스 찾기
        mid = end
        for i in range(start + 1, end):
            if tree[start] < tree[i]:
                mid = i  # i부터 오른쪽 서브 트리
                break

        postorder(tree, start + 1, mid)  # 왼쪽 서브 트리 순회
        postorder(tree, mid, end)  # 오른쪽 서브 트리 순회

    # 서브 트리의 루트 출력
    print(tree[start])


postorder(tree, 0, len(tree))
