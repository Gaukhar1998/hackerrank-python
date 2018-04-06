A, _ = set( map(str, input().split()) ), input()
b = set().union(input().split(), input().split())
print(A.issuperset(b))

#another solution
A = set( map(str, input().split()) )
b = set()
for i in range(int(input())):
    b.add(A.issuperset( set(map(str, input().split()))) )
print(all(b))
