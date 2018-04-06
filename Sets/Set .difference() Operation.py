_,a,_,b=[set(input().split()) for _ in '1234'];print(len(a-b))

#another solution
n, m = [set(input().split())for _ in range(4)][1::2]
print(len(n - m))

#another solution
a, b = [set(input().split()) for _ in range(4)][1::2]
print (len(a.difference(b)))

#another solution
a , b = [set(input().split()) for _ in range(4)][1::2];print (len(a)-len(a&b))
