a=int(input())
answer=[]
for i in range(a):
    b=int(input())
    answer.append(b)
answer.sort()
for i in range(a):
    print(answer[i])