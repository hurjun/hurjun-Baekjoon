A,B,C=map(int,input().split())
print(-1 if B-C>=0 else A//(C-B)+1)
