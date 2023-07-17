a=input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
answer=0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            answer+=dial.index(j)+3
print(answer)