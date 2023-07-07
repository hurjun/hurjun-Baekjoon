answer=[]
a,b=map(int,input().split())
for i in range(a):
    answer.append(i+1)
for i in range(b):
    x,y=map(int, input().split())
    temp=answer[x-1:y]
    temp.reverse()
    answer[x-1:y]=temp
print(*answer)