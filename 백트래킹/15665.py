"""
15665번: N과 M (11)
https://www.acmicpc.net/problem/15665
"""
from itertools import product

N, M = map(int, input().split())
numbers = sorted(set(input().split()), key=lambda x: int(x))
products = product(numbers, repeat=M)

print("\n".join(map(" ".join, products)))
