# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

N = int(input())
A = list(map(int, input().split()))

operations = 0
all_even = all(num%2 == 0 for num in A)

while all_even:
    A = [num//2 for num in A]
    operations += 1
    all_even = all(num%2 == 0 for num in A)
    
print(operations)