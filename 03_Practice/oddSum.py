# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y<x : 
        x, y = y, x
    total_sum = 0
    for i in range(x+1, y):
        if i % 2 == 1:
            total_sum += i    
    print(total_sum)
