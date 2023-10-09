# https://atcoder.jp/contests/arc087/tasks/arc087_a

from collections import Counter

def solve(N, a):
    cnt = Counter(a)
    res = 0
    for p in cnt.items():
        if p[0] > p[1]:
            res += p[1]
        else:
            res += p[1]-p[0]
    print(res)

N = int(input())
a = list(map(int, input().split()))
solve(N, a)