A,B,V=map(int,input().split())
K=(V-B)/(A-B)
print(int(K) if int(K)==K else int(K)+1)
