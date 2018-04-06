n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))

#another solution
n = input()
s = set(map(int, input().split())) 
for _ in range(int(input())):
    x = list(input().split())
    eval('s.{0}({1})'.format(*x+['']))
print (sum(s))

#another solution
n = int(input())
s = set(map(int, input().split())) 
t = int(input())
for i in range(t):
    c, *args = map(str,input().split())
    getattr(s,c) (*(int(x) for x in args))
print (sum(s))

#another solution
n = int(input())
s = set(map(int, input().split())) 
for _ in range(int(input())):
    opt = input().split()
    if 'pop' == opt[0]: s.pop()
    elif 'remove' == opt[0]: s.remove(int(opt[1]))
    elif 'discard' == opt[0]: s.discard(int(opt[1]))
print(sum(s))

#another solution
n = int(input())
s = set(map(int, input().split())) 
N = int(input())
methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}
for _ in range(N):
    method, *args = input().split()
    methods[method](*map(int,args))
print(sum(s))
