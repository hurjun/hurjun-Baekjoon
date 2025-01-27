def solution(arr):
    a=len(arr)
    b=len(arr[0])
    print(a,b)
    if a>b:
        for i in range(len(arr)):
            for j in range(a-b):
                arr[i].append(0)
    elif a<b:
        tmp=[0 for i in range(b)]
        for i in range(b-a):
            arr.append(tmp)
    print(arr)
    return arr
