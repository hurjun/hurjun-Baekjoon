a, b = map(int, input().split())
answer = []
for i in range(a):
    answer.append(i + 1)
for i in range(b):
    x, y = map(int, input().split())
    temp = answer[x - 1]
    answer[x - 1] = answer[y - 1]
    answer[y - 1] = temp
print(*answer)
