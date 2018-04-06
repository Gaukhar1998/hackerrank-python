print(len(set([input().strip() for _ in range(int(input().strip()))])))

#another solution
print(len({input() for _ in range(int(input()))}))

#another solution
n = int(input())
s = set()
for i in range(n):
    s.add(input())
print (len(s))
