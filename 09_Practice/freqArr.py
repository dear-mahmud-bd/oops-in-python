# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/V
n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = {}
for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for i in range(1, m + 1):
    if i in count:
        print(count[i])
    else:
        print(0)