def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        temp = ord(s[i])
        if temp <= 90 and temp + n > 90:
            answer += chr(temp + n - 26)
        elif temp >= 97 and temp + n > 122:
            answer += chr(temp + n - 26)
        elif temp == 32:
            answer += " "
        else:
            answer += chr(ord(s[i]) + n)
    return answer
