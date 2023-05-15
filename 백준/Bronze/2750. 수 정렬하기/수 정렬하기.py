a=int(input())
arr=[]
for _ in range(a):
    b=int(input())
    arr.append(b)

arr.sort()
for i in range(len(arr)):
    print(arr[i])