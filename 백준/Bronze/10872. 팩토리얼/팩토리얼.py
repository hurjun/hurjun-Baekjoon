a=int(input())
b=1
for i in range(1,a+1):
   try:
       b*=i
   except:
       pass

print(b)