a = []
b = []
M, N = map(int, input().split())
for i in range(M):
    i=list(map(int,input().split()))
    a.append(i)
for i in range(M):
    i=list(map(int,input().split()))
    b.append(i)
for i in range(M):
    for j in range(N):
        print(a[i][j]+b[i][j],end=" ")
    print()