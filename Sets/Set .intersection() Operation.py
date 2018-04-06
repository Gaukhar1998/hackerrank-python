num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print (len(st1.intersection(st2)))

#another solution
print(input()==0 or len(set(input().split())&(input()==0 or set(input().split()))))

#another solution
_, sl1 = int(input()), set(map(int,input().split()))
_, sl2 = int(input()), set(map(int,input().split()))
print (len(sl1.intersection(sl2)))

#another solution
n= int(input())
list1 = input().split()
b= int(input())
list2 = input().split()
a = set(list1).intersection(list2)
print (len(a))
