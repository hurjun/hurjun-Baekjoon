def solution(nums):
    answer = 0
    nums.sort()
    temp=list(set(nums))
    if len(temp)<len(nums)//2:
        return len(temp)
    else:
        return len(nums)//2
    