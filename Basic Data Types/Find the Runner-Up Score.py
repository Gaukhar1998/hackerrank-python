i = int(input())
lis = list(map(int,input().strip().split()))[:i]
x=max(lis)
while max(lis)==x:
    lis.remove(max(lis))
print (max(lis))

#another solution
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
