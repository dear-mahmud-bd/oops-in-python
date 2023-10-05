# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F

def calculate_S(X, N):
    S = 0
    power = 0
    while power <= N:
        S += (X ** power)
        power += 2
    return S
X, N = map(int, input().split())
result = calculate_S(X, N)
print(result-1)
