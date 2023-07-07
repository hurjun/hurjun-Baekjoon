answer=[]
for i in range(30):
    answer.append(i+1)
for i in range(28):
    a=int(input())
    answer.remove(a)
answer.sort()
print(answer[0])
print(answer[1])