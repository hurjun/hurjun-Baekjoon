a=int(input())
bag=0
while a>0:
    if a%5==0:
        bag+=a//5

        break

    a-=3
    bag+=1

    if a<0:
        bag=-1

print(bag)
