# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y

def fibonacci(n):
    if n==1: return [0]
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        nxt_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(nxt_num)
    return fib_seq

n = int(input())
result = fibonacci(n)
print(*result)