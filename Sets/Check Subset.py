for i in range(int(input())):
    a, A = int(input()), set(input().split())
    b, B = int(input()), set(input().split())
    print(A.issubset(B))
