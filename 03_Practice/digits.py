# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q
    
t = int(input())
for _ in range(t):
    n = input()
    digits = []
    reverce_num = ""
    for i in range(len(n)):
        digits.append(n[i])
    print(" ".join(digits[::-1]))
