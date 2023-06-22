def solution(numbers):
    answer = 0
    a = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):

            a.append(numbers[i] * numbers[j])
    return max(a)