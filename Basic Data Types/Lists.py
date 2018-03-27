l=[]
for x in range(int(input())):
	s = input().split()
	if hasattr(l,s[0]):
		getattr(l,s[0]) (*map(int,s[1:]))
	else:
		print (l)

#another solution
n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print (l)
