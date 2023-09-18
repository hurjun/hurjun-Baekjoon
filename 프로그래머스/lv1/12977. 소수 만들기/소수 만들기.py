def solution(nums):
    answer=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sosu=nums[i]+nums[j]+nums[k]
                sosu1=0
                for l in range(2,sosu):
                    if sosu%l==0:
                        sosu1+=1
                        break
                if sosu1==0:
                    answer+=1      
    return answer