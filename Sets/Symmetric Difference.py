a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')

#another solution
a,b = [set(input().split()) for _ in range(4)][1::2]
print('\n'.join(sorted(a^b, key=int)))

#third solution
_,a=input(),set(map(int, ((input().split()))))
_,b=input(),set(map(int, ((input().split()))))
c = sorted(a ^ b)
for i in c:
    print(i)
