def solution(s):
    answer = ""
    num=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i,nums in enumerate(num):
        s=s.replace(nums,str(i))
    
    return int(s)