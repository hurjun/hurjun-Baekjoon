answer=0
a=input()
b=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in range(len(b)):
    if b[i] in a:
        answer+=a.count(b[i])

print(len(a)-answer)