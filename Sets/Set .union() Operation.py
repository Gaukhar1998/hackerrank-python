e="(set(input().split())if input()!='-1'else '')";print(len(eval(e)|eval(e)))

#another solution
_,a,_,b=eval("set(input().split()),"*4);print(len(a|b))

#another solution
_,n,_,b = (set(input().split()) for _ in range(4))
print(len(n|b))

#another solution
print(input() == 0 or len(set(input().split()).union(input() == 0 or input().split())))

#another solution
_,a,_,b=input(),set(input().split()),input(),set(input().split())
print(len(a|b))
