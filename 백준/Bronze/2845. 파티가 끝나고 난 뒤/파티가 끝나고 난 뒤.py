a, b = map(int, input().split())
c=list(map(int, input().split()))
for i in range(5):
    c[i]=c[i]-a*b
print(*c)