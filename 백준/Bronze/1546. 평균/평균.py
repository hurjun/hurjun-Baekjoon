a=int(input())
b=list(map(int,input().split()))
c=max(b)
answer=0
for i in range(a):
    answer+=b[i]*100/c
print(answer/a)