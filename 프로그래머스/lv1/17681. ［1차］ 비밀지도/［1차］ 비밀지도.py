def solution(n, arr1, arr2):
    answer = []
    array1=[]
    for i in range(n):
        temp1=list(str(bin(arr1[i])))
        del temp1[0]
        del temp1[0]
        while len(temp1)<n:
            temp1.insert(0,"0")
        temp2 = list(str(bin(arr2[i])))
        del temp2[0]
        del temp2[0]
        while len(temp2) < n:
            temp2.insert(0, "0")
        temp3=""
        for j in range(n):
            if temp1[j]=="0" and temp2[j]=="0":
                temp3+=" "
            else:
                temp3+="#"
        answer.append(temp3)



    return answer