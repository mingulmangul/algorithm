"""
1991번 트리 순회: https://www.acmicpc.net/problem/1991

재귀
- 입력
  1. 배열에 트리 저장 -> 크기가 매우 커질 수 있음
  2. 연결 리스트에 트리 저장 -> 구현이 어려움
  3. 딕셔너리에 트리 저장
- 한 함수에서 전위순회 -> 중위순회 -> 후위순회
"""
import sys
input = sys.stdin.readline

def traverse(tree, v, preorder, inorder, postorder):
    if v == '.':
        return
    preorder.append(v)
    traverse(tree, tree[v][0], preorder, inorder, postorder)
    inorder.append(v)
    traverse(tree, tree[v][1], preorder, inorder, postorder)
    postorder.append(v)

N = int(input().rstrip())
tree = dict()
root, l, r = input().split()
tree[root] = [l, r]
for _ in range(1, N):
    v, l, r = input().split()
    tree[v] = [l, r]

preorder, inorder, postorder = [], [], []
traverse(tree, root, preorder, inorder, postorder)
print(*preorder, sep="")
print(*inorder, sep="")
print(*postorder, sep="")