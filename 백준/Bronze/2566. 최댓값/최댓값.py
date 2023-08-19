arr=[]
for i in range(9):
    a=list(map(int, input().split()))
    arr.append(a)
answer=0
for i in range(9):
    for j in range(9):
        if arr[i][j]>answer:
            answer=arr[i][j]
print(answer)
for i in range(9):
    for j in range(9):
        if arr[i][j]==answer:
            print(i+1,j+1)
