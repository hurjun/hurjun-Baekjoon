a,b=map(int, input().split())
answer=[]
for i in range(a):
    answer.append(0)
for i in range(b):
    x,y,z=map(int, input().split())
    for j in range(x-1,y):
       answer[j]=z
print(*answer)