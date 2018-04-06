input()
L = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split())) 
print(sum(map(int, L)))

#another solution
_, A = int(input()),set(map(int, input().split()))
for _ in range(int(input())):
    command, newSet = input().split()[0],set(map(int, input().split()))
    getattr(A, command)(newSet)
print (str(sum(A)))

#another solution
input()
L = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split())) 
print(sum(map(int, L)))

#another solution
_, a = input(), set(input().split())
for _ in range(int(input())):
    op, *nums = input().split()[0], input().split()
    getattr(a, op)(*nums)
print(sum(map(int, a)))

#another solution
m = int(input())
A = set(map(int, input().split()))
n = int(input())
for i in range(n):
    cmd, args = input().split()
    B = set(map(int, input().split()))
    eval('A.'+cmd+'(B)')
print (sum(A))

#another solution
S = input() == 0 or set(input().split())
[getattr(S, input().split()[0])(input().split()) for _ in range(int(input()))]
print(sum(map(int, S)))
