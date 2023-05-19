def solution(arr):
    answer = []
    for i in range(len(arr)):
        if int(arr[i])>=50 and int(arr[i])%2==0:
            answer.append(int(arr[i])//2)
        elif int(arr[i])<50 and int(arr[i])%2==1:
            answer.append(int(arr[i])*2)
        else:
            answer.append(int(arr[i]))
    return answer