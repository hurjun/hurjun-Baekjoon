def solution(arr):
    n=0
    while len(arr)!=2**n:
        if len(arr)==2**n:
            break
        if len(arr)>2**n:
            n+=1
        elif len(arr)<2**n:
            for _ in range(2**n-len(arr)):
                arr.append(0)
            break
    return arr