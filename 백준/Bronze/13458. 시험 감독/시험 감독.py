N=int(input())
A=list(map(int, input().split()))
B,C=map(int,input().split())
answer=0
for i in range(N):
    D=A[i]-B
    if D>0:
        if D%C==0:
            answer+=D//C
        else:
            answer+=D//C+1
print(answer+N)