def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in range(1,len(arr)):
        if arr[i-1]!=arr[i]:
            answer.append(arr[i-1])
    
    answer.append(arr[-1])
    return answer