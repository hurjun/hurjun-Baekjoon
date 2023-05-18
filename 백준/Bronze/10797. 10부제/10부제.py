a=int(input())
b=list(map(int,input().split()))
cnt=0
for i in range(len(b)):
    if a==b[i]:
        cnt+=1
print(cnt)