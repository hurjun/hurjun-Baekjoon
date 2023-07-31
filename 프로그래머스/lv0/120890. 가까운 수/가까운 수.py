def solution(array, n):
    answer = 0
    box=[]
    array.sort()
    for i in array:
        box.append(abs(i-n))
    answer=[array[box.index(min(box))]]
    return answer[0]