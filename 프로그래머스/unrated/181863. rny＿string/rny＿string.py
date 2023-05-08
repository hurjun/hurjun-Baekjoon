def solution(rny_string):
    a=list(rny_string)
    for i in range(len(a)):
        if a[i]=="m":
            a[i]="rn"
  
    answer = ''.join(a)
    return answer