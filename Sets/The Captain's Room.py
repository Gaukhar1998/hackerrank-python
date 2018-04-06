k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))

#another solution
d=int(input())
a=input().split()
s1,s2=set(),set()
for i in a:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print(list(s3)[0])

#another solution
from collections import Counter  
_ = int(input().strip())  
a = map(int, input().split())  
nums = Counter(a)  
print(min(nums, key=nums.get))

#another solution
s = sorted([input().split() for _ in range(2)][1])
print((set(s[0::2]) ^ set(s[1::2])).pop())

#another solution
if __name__ == "__main__":
    K = int(input())
    rooms = input().split()
    rooms.sort()
    a = set([rooms[i] for i in range(0,len(rooms),2)])
    b = set([rooms[i] for i in range(1,len(rooms),2)])
    print(list(a.symmetric_difference(b))[0])
