n1=int(input())
S1=set(map(int,input().split()))
n2=int(input())
S2=set(map(int,input().split()))
print(len(S1.symmetric_difference(S2)))

#another solution
_, S1 = int(input()), set(map(int,input().split()))
_, S2 = int(input()), set(map(int,input().split()))
print(len(S1.symmetric_difference(S2)))

#another solution
a , b = [set(input().split()) for _ in range(4)][1::2];print (len(a^b))
